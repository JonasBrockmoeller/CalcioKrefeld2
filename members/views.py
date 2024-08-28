import json
from datetime import datetime

from django.http import HttpResponse, JsonResponse

from clubs.models import Club
from members.models import Member
from prognosis.models import Prognosis
from results.models import Result


def get_members(request):
    members = Member.objects.all().values()
    print(members)
    return HttpResponse(members)

def new_member(request):
    member_instance = None
    print("request for new member received!")
    try:
        # Use default values if the request body is empty
        if not request.body:
            print("no body problem")
        else:
            data = json.loads(request.body)

            member_id = data.get('appleId')
            member_email = data.get('email')
            member_firstname = data.get('firstname')
            member_lastname = data.get('lastname')

            if member_id not in Member.objects.all().values_list('appleId', flat=True):
                print("adding user")
                member_instance = Member.objects.create(appleId=member_id, email=member_email, firstname=member_firstname, lastname=member_lastname)
                prognosis_instance = Prognosis.objects.create(created_by=member_id,
                                                              created_on=datetime.now(),
                                                              prognosis_champion='',
                                                              prognosis_topscorer='',
                                                              prognosis_trainer_fired='',
                                                              prognosis_surprise='',
                                                              prognosis_disappointment='',
                                                              prognosis_hottake=''
                                                              )
                result_instance = Result.objects.create(
                    created_by=member_id,
                    created_on=datetime.now(),
                    homeranking=get_multiline_string(),
                    awayranking=get_multiline_string(),
                    logoranking=get_multiline_string()
                )
            else:
                print("User exists already in DB")


    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON in request body'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

    return HttpResponse(member_instance)

def get_multiline_string():
    return """[
  {
    "specialkit" : "",
    "homekit" : "https:\/\/www.dropbox.com\/scl\/fi\/rvwnj4r46mzjfx9mqjhme\/Wolfsburg.png?rlkey=9jgf2g9uxzqlj3w6fjw6352ez&st=owfeplxn&raw=1",
    "awaykit" : "https:\/\/www.dropbox.com\/scl\/fi\/36pcor2p4uyzkoh3pv4yy\/Wolfsburg.png?rlkey=x8ap8e9opqx5cyw0sc28khlah&st=ghuit040&raw=1",
    "logo" : "https:\/\/www.dropbox.com\/scl\/fi\/t4epb089tu23fhptqivbp\/VfL_Wolfsburg.png?rlkey=595itn707ibi4pvc3ufhwigh4&st=lzuj4z38&raw=1",
    "name" : "VfL Wolfsburg"
  },
  {
    "awaykit" : "https:\/\/timvandevall.com\/wp-content\/uploads\/2014\/06\/blank-tshirt-template.jpg",
    "specialkit" : "",
    "homekit" : "https:\/\/timvandevall.com\/wp-content\/uploads\/2014\/06\/blank-tshirt-template.jpg",
    "name" : "VfL Bochum",
    "logo" : "https:\/\/www.dropbox.com\/scl\/fi\/5z7f2sefid645lt0r9f5j\/VfL_Bochum.png?rlkey=7680tpp5ap16m4joytq3xai54&st=4gl0bh75&raw=1"
  },
  {
    "awaykit" : "https:\/\/www.dropbox.com\/scl\/fi\/txodi6jdbt5lxy7t85lud\/Bayer_Leverkusen.png?rlkey=lvawn9w8h617w37djdz77cnmf&st=2e1mqwhm&raw=1",
    "specialkit" : "",
    "homekit" : "https:\/\/www.dropbox.com\/scl\/fi\/ivl89n1do4de4mmmdk7pj\/Bayer_Leverkusen.png?rlkey=e3ly3l8i076wt2ap9d0y7fzxx&st=7y4sl6qe&raw=1",
    "name" : "Bayer 04 Leverkusen",
    "logo" : "https:\/\/www.dropbox.com\/scl\/fi\/8bvgfqknxg0vjm3l2fn0t\/Bayer_Leverkusen.png?rlkey=5xzffjmpv9lpqog5rcqf1q4hl&st=2yijqll8&raw=1"
  },
  {
    "specialkit" : "",
    "logo" : "https:\/\/www.dropbox.com\/scl\/fi\/4c64j2fkvrlh5exj2zck2\/FC_Augsburg.png?rlkey=64y8eg3ixib329e8kpf6z4fze&st=u4isi00b&raw=1",
    "awaykit" : "https:\/\/timvandevall.com\/wp-content\/uploads\/2014\/06\/blank-tshirt-template.jpg",
    "name" : "FC Augsburg",
    "homekit" : "https:\/\/www.dropbox.com\/scl\/fi\/31mq4m2f91zzuny8c6e0b\/FC-Augsburg.png?rlkey=lfdpuz97nhcy3upjb42p8ea2l&st=yzh25az6&raw=1"
  },
  {
    "homekit" : "https:\/\/www.dropbox.com\/scl\/fi\/dzsfz7yf2ysjfmgxl736k\/Werder-Bremen.png?rlkey=27fjosmob4cmsou706veli8da&st=pw8h0lwn&raw=1",
    "awaykit" : "https:\/\/timvandevall.com\/wp-content\/uploads\/2014\/06\/blank-tshirt-template.jpg",
    "name" : "SV Werder Bremen",
    "logo" : "https:\/\/www.dropbox.com\/scl\/fi\/b0kj7m6r0jifg3j0r8pbc\/Werder-Bremen-Logo.png?rlkey=h4xlq2pav5n6zhu46jxus5uro&st=k7jy582e&raw=1",
    "specialkit" : ""
  },
  {
    "homekit" : "https:\/\/www.dropbox.com\/scl\/fi\/2v2p3wbty0ze4a7r36iif\/1-fc-heidenheim-trikot.png?rlkey=qjczfyhu7zqal21f0vlr1962o&st=0z6x6qdr&raw=1",
    "name" : "1. FC Heidenheim 1846",
    "logo" : "https:\/\/www.dropbox.com\/scl\/fi\/9r59h7zaow0uug1yiqxao\/1._FC_Heidenheim.png?rlkey=ecnwh1jfqgxngr3mumrsj7uzs&st=97k8r6bk&raw=1",
    "awaykit" : "https:\/\/www.dropbox.com\/scl\/fi\/qofwfe592m8dj8m6f9ztl\/Heidenheim.png?rlkey=lr68en2liymcptr14k4k8gct1&st=tcxchuzw&raw=1",
    "specialkit" : ""
  },
  {
    "name" : "RasenBallsport Leipzig",
    "logo" : "https:\/\/www.dropbox.com\/scl\/fi\/4ko3g3xcew1qxibo0tj2a\/RB_Leipzig.png?rlkey=zu8x5d0mdmgcqzd7chfvrsaq0&st=ajht5l89&raw=1",
    "specialkit" : "",
    "awaykit" : "https:\/\/www.dropbox.com\/scl\/fi\/iknvubusgmmg5bgfysitt\/RB_Leipzig.png?rlkey=d0h5dofuvorpmxv2wden6ljb0&st=hhsno0gz&raw=1",
    "homekit" : "https:\/\/www.dropbox.com\/scl\/fi\/owvbfd2pnd5qea3zlv50c\/RB_Leipzig.png?rlkey=v2a62a8ikon74i5usnq4twume&st=5g9rtgt6&raw=1"
  },
  {
    "awaykit" : "https:\/\/timvandevall.com\/wp-content\/uploads\/2014\/06\/blank-tshirt-template.jpg",
    "name" : "TSG 1899 Hoffenheim",
    "homekit" : "https:\/\/www.dropbox.com\/scl\/fi\/tu9iay31aeem8bb69ghtf\/TSG_Hoffenheim.png?rlkey=csxjeeuc5el09tu8tgo3bgt9r&st=fvjjw92e&raw=1",
    "specialkit" : "",
    "logo" : "https:\/\/www.dropbox.com\/scl\/fi\/gnq1kkaowz3kkuvdawrzj\/TSG_Hoffenheim.png?rlkey=c682rgkcrxlaj80u5s5mjojfy&st=yy2h06sb&raw=1"
  },
  {
    "logo" : "https:\/\/www.dropbox.com\/scl\/fi\/k31wyc8uuixb4li2jekx6\/Moenchengladbach.png?rlkey=744fk5du0hewpokvmtzey9fol&st=gkyktdqz&raw=1",
    "specialkit" : "",
    "name" : "Borussia Mönchengladbach",
    "homekit" : "https:\/\/www.dropbox.com\/scl\/fi\/5to8lmkzej3e130mpv9lu\/Moenchengladbach.png?rlkey=xp8ibgvjzykqrq7c143uwxh28&st=2m4ormi0&raw=1",
    "awaykit" : "https:\/\/www.dropbox.com\/scl\/fi\/k8oiitutq3je2f9xbhb2m\/Moenchengladbach.png?rlkey=hlyt8hsl9ufm90qcoq26cjxne&st=tbu8jvyl&raw=1"
  },
  {
    "logo" : "https:\/\/www.dropbox.com\/scl\/fi\/3hb9rbdli4csmjvq2butb\/Eintracht_Frankfurt.png?rlkey=ec1t1u5oa1ys45kh4ica2icpt&st=7270odrt&raw=1",
    "awaykit" : "https:\/\/timvandevall.com\/wp-content\/uploads\/2014\/06\/blank-tshirt-template.jpg",
    "name" : "Eintracht Frankfurt",
    "homekit" : "https:\/\/www.dropbox.com\/scl\/fi\/a9affkrdnukuehe1cogwp\/eintracht-frankfurt.png?rlkey=onosab09fbsljoxflyjqi0izo&st=kentwmgt&raw=1",
    "specialkit" : ""
  },
  {
    "specialkit" : "",
    "name" : "FC St. Pauli",
    "logo" : "https:\/\/www.dropbox.com\/scl\/fi\/7l5brl5v1b8963j2n48zh\/st_pauli.png?rlkey=xslijih8xex0l9klou7hfsqg8&st=cswxbjkd&raw=1",
    "homekit" : "https:\/\/www.dropbox.com\/scl\/fi\/ndpegcz8fmygkglo4uj3y\/st-pauli.png?rlkey=xlctr9u6zbo3ztpdna311cqb1&st=lnqtqj4l&raw=1",
    "awaykit" : "https:\/\/www.dropbox.com\/scl\/fi\/53ka55aiu3j9txhilp2on\/st-pauli.png?rlkey=1g3q344qywioodlneku2v1fkv&st=9plq401k&raw=1"
  },
  {
    "logo" : "https:\/\/www.dropbox.com\/scl\/fi\/0314co6pemr1q5c1hqpzh\/1-FC-Union-Berlin.png?rlkey=yih7usajrwnm71ju5qyc8dt6r&st=iza496g0&raw=1",
    "name" : "1. FC Union Berlin",
    "homekit" : "https:\/\/timvandevall.com\/wp-content\/uploads\/2014\/06\/blank-tshirt-template.jpg",
    "awaykit" : "https:\/\/timvandevall.com\/wp-content\/uploads\/2014\/06\/blank-tshirt-template.jpg",
    "specialkit" : ""
  },
  {
    "name" : "FC Bayern München",
    "logo" : "https:\/\/www.dropbox.com\/scl\/fi\/hlw69cix3cp6n8zjspnbc\/FC_Bayern_M-nchen.png?rlkey=6fzteljqjghh17lipckr85ld2&st=4hplqv4c&raw=1",
    "specialkit" : "",
    "homekit" : "https:\/\/www.dropbox.com\/scl\/fi\/3gw79fuesvmstga4q3pdn\/fc-bayern-muenchen.png?rlkey=rxue9djk5ppp2sz3milws8osw&st=c5nb5t82&raw=1",
    "awaykit" : "https:\/\/www.dropbox.com\/scl\/fi\/ohrm79v33cfnzbqpxfn45\/fc-bayern-muenchen.png?rlkey=b120z7sm7tzmagnbds7byp8bw&st=7mgsx981&raw=1"
  },
  {
    "logo" : "https:\/\/www.dropbox.com\/scl\/fi\/dge4gz2ok8hyd9iz6912m\/kiel.png?rlkey=zelcujbwmf6ydzz8w2hobv2c3&st=pecs4nax&raw=1",
    "name" : "Holstein Kiel",
    "homekit" : "https:\/\/www.dropbox.com\/scl\/fi\/hh2mvppku64sxnglkap3s\/Kiel.png?rlkey=fqk05ae31epk7qpk4fgpqgl8z&st=azqmp77s&raw=1",
    "awaykit" : "https:\/\/www.dropbox.com\/scl\/fi\/mqi32wlmg4vehh209qfe6\/kiel.png?rlkey=5j1dfiyesxh9749c58aw407rr&st=t7d9ehhc&raw=1",
    "specialkit" : ""
  },
  {
    "awaykit" : "https:\/\/timvandevall.com\/wp-content\/uploads\/2014\/06\/blank-tshirt-template.jpg",
    "specialkit" : "",
    "logo" : "https:\/\/www.dropbox.com\/scl\/fi\/w7pvg3v83nph27gy9gg72\/VfB-Stuttgart.png?rlkey=8c8n6oeu3jxrmgrvr7ptv3y8d&st=pgxh9ihf&raw=1",
    "name" : "VfB Stuttgart",
    "homekit" : "https:\/\/www.dropbox.com\/scl\/fi\/p6xi9qq8zffmhr2i9mu4n\/VFB-Stuttgart.png?rlkey=buszro0crtr0fqep59bvppt4x&st=5t96iw9t&raw=1"
  },
  {
    "awaykit" : "https:\/\/www.dropbox.com\/scl\/fi\/hegmkx6x5xckl02oj8e2j\/Mainz-05.png?rlkey=gdntgj49zb6mq26n35bxn4ayr&st=j1t566s4&raw=1",
    "specialkit" : "",
    "homekit" : "https:\/\/www.dropbox.com\/scl\/fi\/7pasg1xbn56vdjrxwbh4o\/FSV-Mainz-05.png?rlkey=k0yl6wkb0i4tksi8tpxxlq8al&st=diaal8vg&raw=1",
    "name" : "1. FSV Mainz 05",
    "logo" : "https:\/\/www.dropbox.com\/scl\/fi\/kvmzz8fhlbuv802r5wqps\/FSV_Mainz_05.png?rlkey=an8lbopgsjrj2wd0tzo6114x2&st=ubw43cfv&raw=1"
  },
  {
    "homekit" : "https:\/\/www.dropbox.com\/scl\/fi\/8qso9f8ystbc5f4aayp5h\/BVB.png?rlkey=xxni10ddpjtvaww39231myex0&st=ne3w5ooa&raw=1",
    "logo" : "https:\/\/www.dropbox.com\/scl\/fi\/waytnu59vhc5c1d4d1au7\/BVB.png?rlkey=z2ynrz84nk8qcze4u2pko1z3u&st=x8a0y5w4&raw=1",
    "specialkit" : "",
    "awaykit" : "https:\/\/timvandevall.com\/wp-content\/uploads\/2014\/06\/blank-tshirt-template.jpg",
    "name" : "Borussia Dortmund"
  },
  {
    "awaykit" : "https:\/\/www.dropbox.com\/scl\/fi\/cjhcw12t8x0i3e9oo3yuc\/SC-Freiburg.png?rlkey=d71dkjp7kufa1wi5tefp0npzw&st=ke28r0fb&raw=1",
    "homekit" : "https:\/\/www.dropbox.com\/scl\/fi\/m6hklpixk74vv7bjfnlwa\/SC-Freiburg.png?rlkey=k0uupxz999t66iliptotc4phj&st=cfiocets&raw=1",
    "logo" : "https:\/\/www.dropbox.com\/scl\/fi\/bn16w6cauurdxzca80hha\/SC_Freiburg.png?rlkey=kpnwwfdn07bhsud64fiacshi9&st=ylk74ys4&raw=1",
    "specialkit" : "",
    "name" : "SC Freiburg"
  }
]"""