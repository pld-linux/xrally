%define name xrally
%define version 0.9
%define release 1mdk

Summary: clone of the Rally X arcade game
Name: %{name}
Version: %{version}
Release: %{release}
Source0:  ftp://ftp.linuxgames.com/xrally/%{name}-%{version}.tar.bz2
Copyright: GPL
Group: Games/Arcade
BuildRoot: /tmp/%{name}-buildroot
Prefix: %{_prefix}

%description
XRally is a clone of the Rally X arcade game. In Rally X, you control a blue car
which has to run through a maze-like level collecting flags and avoiding
colliding with enemy (red) cars. In order to protect itself, the blue car can
discharge clouds of smoke which stun the enemy cars for a while. The enemy cars
can also crash into each other, what gives you some extra time. One of the main
features of XRally is that it is fully customizable. You can create custom
tilesets and levels and load them at run time, changing the entire look of the
game. (You could, for instance, create a water tileset, using boats instead of
cars.)

%prep
%setup -n %{name}
rm maps/"Test Level"

%build
%configure
make CFLAGS="%{optflags}"

%install
rm -rf $RPM_BUILD_ROOT
make install prefix=$RPM_BUILD_ROOT%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS BUGS NEWS README TODO %{name}.lsm
/usr/bin/%{name}
/usr/share/%{name}

%changelog
* Thu Mar  9 2000 Pixel <pixel@mandrakesoft.com> 0.9-1mdk
- new version

* Sun Feb 13 2000 Pixel <pixel@mandrakesoft.com> 0.8-1mdk
- initial spec


# end of file
