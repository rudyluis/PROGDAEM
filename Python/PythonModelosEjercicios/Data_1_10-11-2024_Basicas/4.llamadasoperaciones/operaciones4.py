def operacion1(a,c,e,sig1,sig2):
    if(sig1==sig2):
        match sig1:
            case '+':
                resul=a+c+e
            case '-':
                resul=a-c-e
            case '*':
                resul=a*c*e
            case '/':
                resul=a/c/e
    else:
        if(sig1 in('+','-') and sig2 in('+','-')):
            match sig1:
                case '+':
                    resul=a+c-e
                case '-':
                    resul=a-c+e
        else:
            if(sig1 in('+','-') and sig2 in('*','/')):
                match sig2:
                    case '*':
                        resul=c*e
                    case '/':
                        resul=c/e
                match sig1:
                    case '+':
                        resul=a+resul
                    case '-':
                        resul=a-resul
            if(sig1 in('*','/') and sig2 in('+','-')):
                match sig1:
                    case '*':
                        resul=a*c
                    case '/':
                        resul=a/c
                match sig2:
                    case '+':
                        resul=resul+e
                    case '-':
                        resul=resul-e
            if(sig1 in('*','/') and sig2 in('*','/')):
                match sig1:
                    case '*':
                        resul=a*c
                    case '/':
                        resul=a/c
                match sig2:
                    case '*':
                        resul=resul*e
                    case '/':
                        resul=resul/e
    print('>>>>',resul)