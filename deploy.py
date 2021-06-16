from chatbot import searcher ,enocoder,decoder ,voc
encoder.eval()
decoder.eval()

# Initialize search module
searcher = GreedySearchDecoder(encoder, decoder)



evaluateInput(encoder, decoder, searcher, voc)