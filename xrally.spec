Summary:	Clone of the Rally X arcade game
Summary(pl):	Klon gry Rally X
Name:		xrally
Version:	1.1
Release:	1
License:	GPL
Group:		X11/Applications/Games
# Source0:	ftp://ftp.linuxgames.com/xrally/%{name}-%{version}.tar.gz
Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/xrally/%{name}-%{version}.tar.bz2
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-DESTDIR.patch
URL:		http://www.linuxgames.com/xrally/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

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

%prep
%setup -q -n %{name}
%patch -p1
rm -f maps/"Test Level"

%build
rm -f missing
aclocal
%{__autoconf}
%{__automake}
%configure
%{__make} CFLAGS="%{optflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Games/Arcade,%{_pixmapsdir}}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Games/Arcade
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

gzip -9nf AUTHORS NEWS README TODO %{name}.lsm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_datadir}/xrally
%{_applnkdir}/Games/Arcade/*
%{_pixmapsdir}/*
