import logging

from dependency_injector.wiring import Provide, inject

logger = logging.getLogger(__name__)


class DatabaseTransactionManager:
    @inject
    def __init__(
        self, db_connector: SQLAlchemyDatabaseConnector = Provide["db_connector"]
    ):
        self._db = db_connector

    def get_transaction(self) -> Transaction:
        logger.debug("Trying to find already opened session")
        current_session = SessionHolder.session.get()
        if current_session:
            transaction = Transaction(is_new=False)
            logger.debug(
                "Use already opened session at transaction '%s'", str(transaction.id)
            )
        else:
            transaction = Transaction(is_new=True)
            logger.debug(
                "Prepare to open a new session at transaction '%s'", str(transaction.id)
            )
            session = self._db.session_maker()
            logger.debug(
                "Session was opened successfully at transaction '%s'",
                str(transaction.id),
            )
            SessionHolder.set_session(session)
        return transaction

    def commit(self, transaction: Transaction) -> None:
        if transaction.is_new:
            session = SessionHolder.get_session()
            try:
                logger.debug("Prepare to commit transaction '%s'", transaction.id)
                session.commit()
                logger.debug("Transaction '%s' commited", transaction.id)
            except Exception as commit_error:
                try:
                    session.rollback()
                except Exception as rollback_error:
                    logger.error(
                        f"Transaction {transaction.id} could not rollback session. Reason: {rollback_error}."
                    )
                raise commit_error
            finally:
                SessionHolder.detach_session()
                try:
                    logger.debug(
                        "Prepare to close session at transaction '%s'", transaction.id
                    )
                    session.close()
                    logger.debug(f"Session {transaction.id} closed.")
                except Exception as e:
                    logger.warning(
                        f"Session {transaction.id} could not close session. Reason: {e}."
                    )
        else:
            logger.info(f"Transaction {transaction.id} will be committed.")
        transaction.detach_from_context()

    def rollback(self, transaction: Transaction) -> None:
        if transaction.is_new:
            session = SessionHolder.get_session()
            SessionHolder.detach_session()
            try:
                logger.debug("Prepare to rollback transaction '%s'", transaction.id)
                session.rollback()
                logger.debug(f"Transaction {transaction.id} rolled back.")
            except Exception as e:
                logger.warning(f"Transaction {transaction.id}. Error on rollback: {e}.")
                raise e
            finally:
                try:
                    logger.debug(
                        "Prepare to close session at transaction '%s'", transaction.id
                    )
                    session.close()
                    logger.debug(f"Session {transaction.id} closed.")
                except Exception as e:
                    logger.warning(
                        f"Transaction {transaction.id}. Error on closing: {e}."
                    )
        else:
            transaction.is_failed.set(True)
            logger.debug(f"Transaction {transaction.id} will be rolled back.")
        transaction.detach_from_context()
