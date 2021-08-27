import logging
import ask_sdk_core.utils as ask_utils

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model import Response

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)



class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = '<speak> <amazon:domain name="long-form"> <amazon:emotion name="disappointed" intensity="high"> Welcome to tapping for anxiety. Please state your stress level and whether you want a long or short session. </amazon:emotion></amazon:domain></speak>'
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class CaptureStressLevelIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("CaptureStressLevelIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        slots = handler_input.request_envelope.request.intent.slots
        global stressNumSlot
        stressNumSlot = slots["stressNumSlot"].value
        global time
        time = slots["time"].value
        
        speak_output = '<speak> <amazon:domain name="long-form"> <amazon:emotion name="disappointed" intensity="high">Your stress level is {stressNumSlot} and you want a {time} minute session correct?  </amazon:emotion></amazon:domain></speak>'.format(stressNumSlot=stressNumSlot,time=time)

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


class startSessionIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("startSessionIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        global time
        timeSet = time
        
        if timeSet == "short":
            speak_output = '<speak> <amazon:domain name="long-form"> <amazon:emotion name="disappointed" intensity="high"> <amazon:effect name="whispered"> <prosody rate = "90%"> Okay, starting a short session .  Begin by getting comfortable. You can sit or stand or lay. You can close your eyes if you are in a safe and comfortable place to do so. Let’s begin . First, begin by using your index finger to slowly, but firmly, tap along your eyebrow ridge  Tap . Tap . Tap . As your tap move your finger from the bridge of the nose outward . Tap . Tap . Tap . We will spend a brief moment here. As you tap become aware of your breathing .  Tap . Tap . Tap . We are about to move position but first take a deep breath in . <break time="4s"/> . Now, using your finger tips from your eyebrow ridges to your cheekbones and begin to firmly . but slowly .  Tap . Tap . Tap . Good, now tap along the orbital bone that goes from the peak of your cheeks, to right under your eyes .  Tap . Tap . Tap . . We will stay here, tapping along the orbital bone for a minute . Take this moment to think about what is maxing you anxious <break time="4s"/> . Try to name your anxiety .  Tap . Tap . Tap . Where is your anxiety coming from?  Tap . Tap . Tap . Now, prepare to move. Using your left hand begin tapping on the side of your right index finger.  Tap . Tap . Tap . Say or think deeply about the name of your anxiety. Imagine how the name of your anxiety is spelt in your head, or better, say it outloud.  Tap . Tap . Tap . Good job. Your doing great. Now, as you think about what is making you anxious move down your fingers, tapping on your right middle finger.  Tap . Tap . Tap . Wonderful job. Now, move to your middle finger.  Tap . Tap . Tap . Perhaps the thing making you anxious is huge and impossible  Tap . Tap . Tap . Now, move to your ring finger.  Tap . Tap . Tap . Perhaps the thing making you anxious is so scary that you feel paralyzed.  Tap . Tap . Tap . Moving to your littlest finger. Perhaps you will never overcome this anxiety.  Tap . Tap . Tap . We are now going to move to our other hand repeat the process, begining with tapping on the side of your left hands index fingers.  Tap . Tap . Tap . Imagine what it would be like not to have this anxiety.  Tap . Tap . Tap . Moving to your middle finger . Imagine how easy it would be if you didn not feel this way.  Tap . Tap . Tap . Moving to your ring finger, perhaps you can get through this anxiety.  Tap . Tap . Tap . Moving to your littlest finger. Maybe it feels like this anxiety will never go away  Tap . Tap . Tap . Maybe it can.  Tap . Tap . Tap . We are going to move now. With both hands begin tapping on your collar bones.  Tap . Tap . Tap . Maybe you deserve not to feel this anxiety.  Tap . Tap . Tap . Continuing to tap, slowly but firmly, become aware of your breathing once again. Breath in <break time="4s"/> and breath out  Tap . Tap . Tap . One more big breath in, and imagining all the anxiety in you is attaching to the molecules of air you are a about to breath out, let it go with a good loud exhale. You can stop tapping now and open your eyes if you closed them. What is your anxiety level now? Please say, my anxiety level is blank. For example, my anxiety level is 4 or my anxiety level is 3. </prosody></amazon:effect></amazon:emotion></amazon:domain></speak>'
        elif timeSet == "long":
            speak_output = '<speak> <amazon:domain name="long-form"> <amazon:emotion name="disappointed" intensity="high"> <amazon:effect name="whispered"> <prosody rate = "90%"> Okay, starting a short session. Begin by getting comfortable. You can sit, stand, or lay. You can close your eyes if you are in a safe and comfortable place to do so. Lets begin . First, using your index fingers and middle fingers, tap firmly on your eyebrow ridges. Begin where your eyebrows meet your nose and work outward, tapping slowly but firmly. Tap . tap . tap . Good. Take a deep breath in as you tap, expanding your lungs, chest, and even belly. Tap . tap . tap . Exhale. We are about to move positions. But first, continue tapping along your eyebrow ridges and think of what is causing your anxiety? Where does it come from? Tap . tap . tap . Now begin tapping the peak of your cheekbones with all four fingers. Tap . tap . tap . Good. Stay here for a moment and think, what is the name of your anxiety? Tap . tap . tap . While you are thinking of your anxiety, know that your anxiety cannot hurt you. Tap . tap . tap . We are going to move to your hands now. Using your right hand begin tapping on the side of your index finger. Tap . tap . tap . Good. Now move to your middle finger, tapping on its side. Good. Recalling the name of your anxiety, consider what it may be like to not have this fear. Tap . tap . tap . Moving to your ring finger. Tap . tap . tap . Good. Now, move to your pinky finger. Tap . tap . tap . We are going to now switch hands and begin to repeat the process. Slowly tap through your fingers starting with the index finger on your left hand. While you tap, focus on your breathing. Take a deep breath in as you tap, and exhale. Switch fingers. Take a deep breath in as you tap. Switch fingers and exhale. Take a deep breath in as you tap. Switch fingers and exhale. Take a deep breath in as you tap. Switch fingers and exhale. One last time, take a deep breath in as you tap. Switch fingers and exhale. Now, begin tapping on your collar bones with both hands and all your fingers. As you do, breathe, just breath trying your best to make the deepest, slowest breaths you can. Imagine your anxiety sticking to your breathe inside you and being exhaled with each breath. Tap . tap . tap . Good. Keep breathing and tapping. Tap . tap . tap . Take one deep breath in, bigger than any before... and with some noise exhale! Good. Perhaps you are starting to feel a bit better, perhaps not, and that is okay. Using one hand begin tapping on your cupids bow in the space between your nose and upper lip.  Tap . tap . tap . Very good. Anxiety sucks, doesn’t it?  Tap . tap . tap . Moving positions, begin tapping in the space between your bottom lip and your chin. Good. Your anxiety cannot hurt you.  Tap . tap . tap . Now, begin tapping along where on the crown of your forehead. Focus again on your breathing. As you tap with both hands on your forehead take a deep breath in.  Tap . tap . tap . and exhale. Good. Now we are going to start tapping along the side of your body, along the rib cage. Good. We are about to finish. But before we do, recall the name of your anxiety and know that it cannot hurt you. Take one, huge breath in and… release. One more time, still tapping, take a deep breath in. Know that you are safe from your anxiety. Exhale. Last time, take one more massive breath in and exhale. What is your anxiety level now? Please say, my anxiety level is blank. For example, my anxiety level is 4 or my anxiety level is 3.</prosody></amazon:effect></amazon:emotion></amazon:domain></speak>'
        else:
            speak_output = "Sorry, I couldn't understand your requested session time. I hope a short session is okay."
            
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask("What is your anxiety level now? Please say, my anxiet level is blank. For example, my anxiety level is 4 or my anxiety level is 3")
                .response
        )

class NewStressLevelIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("NewStressLevelIntent")(handler_input)
        
    def handle(self, handler_input):
        slots = handler_input.request_envelope.request.intent.slots
        newStressLevel = slots["newAnxietyLevel"].value
        global stressNumSlot
        stressNumSlot = int(stressNumSlot)
        newStressLevel = int(newStressLevel)
        calculatedStress = stressNumSlot - newStressLevel
        
        if calculatedStress <= 0:
            speak_output = 'It seems like your stress went up. To start another session simply say, Alexa, start tapping for anxiety'
        else:
            speak_output = 'During your session your stress level dropped by {calculatedStress} levels.'.format(calculatedStress=calculatedStress)
        return (
            handler_input.response_builder
                .speak(speak_output)
                #.ask
                .response
        )



class HelpIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "You can say hello to me! How can I help?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input) or
                ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Goodbye!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )

class FallbackIntentHandler(AbstractRequestHandler):
    """Single handler for Fallback Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.FallbackIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In FallbackIntentHandler")
        speech = "Hmm, I'm not sure. You can say Hello or Help. What would you like to do?"
        reprompt = "I didn't catch that. What can I help you with?"

        return handler_input.response_builder.speak(speech).ask(reprompt).response

class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        # Any cleanup logic goes here.

        return handler_input.response_builder.response


class IntentReflectorHandler(AbstractRequestHandler):
    """The intent reflector is used for interaction model testing and debugging.
    It will simply repeat the intent the user said. You can create custom handlers
    for your intents by defining them above, then also adding them to the request
    handler chain below.
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        intent_name = ask_utils.get_intent_name(handler_input)
        speak_output = "You just triggered " + intent_name + "."

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Generic error handling to capture any syntax or routing errors. If you receive an error
    stating the request handler chain is not found, you have not implemented a handler for
    the intent being invoked or included it in the skill builder below.
    """
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)

        speak_output = "Sorry, I had trouble doing what you asked. Please try again."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.


sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(CaptureStressLevelIntentHandler())
sb.add_request_handler(startSessionIntentHandler())
sb.add_request_handler(NewStressLevelIntentHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(FallbackIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(IntentReflectorHandler()) # make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers

sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()