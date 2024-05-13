import mood_responses
import text_utils as tils

mood = input("How are you feeling today? ").strip().lower()
print(mood_responses.mood_response(mood))

print(tils.flip_capitalization("aYy....... lMAo"))