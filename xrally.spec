Summary:	Clone of the Rally X arcade game
Summary(es):	Clon del juego Rally X
Summary(pl):	Klon gry Rally X
Summary(pt_BR):	Clone do jogo de fliperama Rally X
Name:		xrally
Version:	1.1
Release:	3
License:	GPL
Group:		X11/Applications/Games
# Source0:	ftp://ftp.linuxgames.com/xrally/%{name}-%{version}.tar.gz
Source0:	http://dl.sourceforge.net/xrally/%{name}-%{version}.tar.bz2
# Source0-md5:	ecb8027508a65a960c0b804ba1f8363c
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-ac_fixes.patch
Patch2:		%{name}-scorefile.patch
URL:		http://www.linuxgames.com/xrally/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
XRally is a clone of the Rally X arcade game. In Rally X, you control
a blue car which has to run through a maze-like level collecting flags
and avoiding colliding with enemy (red) cars. In order to protect
itself, the blue car can discharge clouds of smoke which stun the
enemy cars for a while. The enemy cars can also crash into each other,
what gives you some extra time. One of the main features of XRally is
that it is fully customizable. You can create custom tilesets and
levels and load them at run time, changing the entire look of the
game. (You could, for instance, create a water tileset, using boats
instead of cars.)

%description -l pl
XRally jest klonem gry Rally X. W Rally X mo¿esz kierowaæ niebieskim
samochodem który ma przejechaæ przez labirynty zbiraj±c flagi i
unikaj±c kolizji z wrogimi (czerwonymi) samochodami. Aby siê
zabezpieczyæ, niebieski samochód mo¿e usuwaæ na chwilê k³êby dymu
pozostawiane przez wrogie samochody. Wrogie samochody mog± rozbijaæ
siê wzajemnie, co daje Ci trochê czasu. Jedn± z g³ównych zalet XRally
jest du¿a konfigurowalno¶æ. Mo¿esz tworzyæ w³asne style i poziomy oraz
wczytywaæ je w czasie gry, zmieniaj±c ca³kowicie jej wygl±d. (Mo¿esz
np. stworzyæ styl z wod± i u¿yæ ³odzi zamiast samochodów.)

%description -l pt_BR
O XRally é um clone do jogo de fliperama Rally X. No Rally X, você
controla um carro azul, que corre num labirinto e deve coletar
bandeiras, evitando colidir com os carros (vermelhos) inimigos. Para
se proteger, o carro azul pode disparar nuvens de fumaça que
desnorteiam os carros inimigos por algum tempo. Uma das principais
características do XRally é que ele é completamente configurável. Você
pode criar seus próprios cenários e carregá-los na hora do jogo,
mudando todo seu aspecto gráfico. Você pode por exemplo, criar um
cenário marítimo, usando barcos ao invés de carros.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1
%patch2 -p1
rm -f maps/"Test Level"

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make} CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Games/Arcade,%{_pixmapsdir}} \
	$RPM_BUILD_ROOT%{_localstatedir}/games

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Games/Arcade
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

touch $RPM_BUILD_ROOT%{_localstatedir}/games/%{name}.scores

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO %{name}.lsm
%attr(2755,root,games) %{_bindir}/*
%{_datadir}/xrally
%{_applnkdir}/Games/Arcade/*
%{_pixmapsdir}/*
%attr(664,root,games) %config %verify(not md5 size mtime) %{_localstatedir}/games/%{name}.scores
