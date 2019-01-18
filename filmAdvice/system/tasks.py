from celery.decorators import task
from filmAdvice.system.recomender_engine import recomender_engine
from filmAdvice.system.tools import save_recommendations
from filmAdvice.movie.models import Recommend
import logging


logger = logging.getLogger(__name__)


@task(name="take_predict")
def task_take_predict(user_id):
    try:
        Recommend.objects.filter(user=user_id).delete()
        x_train, x_test, input_layer, output_layer, user_predictions = recomender_engine(user_id)
        logger.info(user_id)
        save_recommendations(user_predictions, user_id)
        logger.info("Save Recommendation is Success")
    except Exception as e:
        logger.warning(e)
