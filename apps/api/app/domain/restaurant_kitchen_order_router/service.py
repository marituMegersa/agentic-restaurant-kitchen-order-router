from sqlalchemy.orm import Session
import uuid
import datetime
from app.domain.restaurant_kitchen_order_router.models import AgenticRestaurantKitchenOrderRouterSession, AgenticRestaurantKitchenOrderRouterItem
from app.domain.restaurant_kitchen_order_router.schemas import AgenticRestaurantKitchenOrderRouterSessionCreate, AgenticRestaurantKitchenOrderRouterItemCreate

class AgenticRestaurantKitchenOrderRouterService:
    @staticmethod
    def create_session(db: Session, data: AgenticRestaurantKitchenOrderRouterSessionCreate) -> AgenticRestaurantKitchenOrderRouterSession:
        db_obj = AgenticRestaurantKitchenOrderRouterSession(
            id=f"SESS-{uuid.uuid4().hex[:8]}",
            task_prompt=data.task_prompt,
            status="COMPLETED",
            safety_tier="GREEN",
            confidence_score=0.98,
            metadata_json=data.metadata_json or {}
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    @staticmethod
    def get_session(db: Session, session_id: str) -> AgenticRestaurantKitchenOrderRouterSession:
        return db.query(AgenticRestaurantKitchenOrderRouterSession).filter(AgenticRestaurantKitchenOrderRouterSession.id == session_id).first()
