Name:       jalv
Version:    1.6.4
Release:    2%{?dist}
Summary:    A simple but fully featured LV2 host for Jack

License:    MIT
URL:        http://drobilla.net/software/jalv/
Source0:    http://download.drobilla.net/%{name}-%{version}.tar.bz2

BuildRequires:  python3
BuildRequires:  doxygen
BuildRequires:  graphviz
BuildRequires:  lilv-devel >= 0.24.0
BuildRequires:  suil-devel >= 0.10.0
BuildRequires:  serd-devel >= 0.24.0
BuildRequires:  sord-devel >= 0.14.0
BuildRequires:  sratom-devel >= 0.6.0
BuildRequires:  lv2-devel >= 1.16.0
BuildRequires:  jack-audio-connection-kit-devel >= 1.9.10
BuildRequires:  qt-devel >= 4.0.0
BuildRequires:  gtk2-devel >= 2.18.0
BuildRequires:  gtk3-devel >= 3.0.0
BuildRequires:  gtkmm24-devel >= 2.20.0
BuildRequires:  qt5-devel >= 5.1.0
BuildRequires:  gcc
BuildRequires:  gcc-c++
Requires:       lv2 >= 1.16.0

%description
%{name} is a simple but fully featured LV2 host for Jack. It runs LV2 plugins 
and exposes their ports as Jack ports, essentially making any LV2 plugin 
function as a Jack application. 

%package qt
Summary:    QT implementation of %{name}
Requires:   %{name}%{_isa} = %{version}-%{release}

%description qt
%{name}-qt is an LV2 host for QT LV2 plugins

%package gtk
Summary:    GTK implementation of %{name}
Requires:   %{name}%{_isa} = %{version}-%{release}

%description gtk
%{name}-gtk is an LV2 host for GTK LV2 plugins

%package gtkmm
Summary:    gtkmm implementation of %{name}
Requires:   %{name}%{_isa} = %{version}-%{release}

%description gtkmm
%{name}-gtkmm is an LV2 host for gtkmm LV2 plugins


%prep
%setup -q 

%build
%set_build_flags
python3 waf configure -v \
 --prefix=%{_prefix} \
 --libdir=%{_libdir} \
 --mandir=%{_mandir} \
 --datadir=%{_datadir} \
 --configdir=%{_sysconfdir} \
 --docs 
python3 waf build -v %{?_smp_mflags}

%install
DESTDIR=%{buildroot} python3 waf install

# Provide a link to the default qt program
ln -fs %{name}.qt4 %{buildroot}%{_bindir}/%{name}.qt

%files
%doc AUTHORS NEWS README.md
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*
%{_libdir}/jack/%{name}.so

%files qt
%{_bindir}/%{name}.qt*
%{_mandir}/man1/%{name}.qt.1.*

%files gtk
%{_bindir}/%{name}.gtk
%{_bindir}/%{name}.gtk3
%{_mandir}/man1/%{name}.gtk.1.*

%files gtkmm
%{_bindir}/%{name}.gtkmm
%{_mandir}/man1/%{name}.gtkmm.1.*

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 07 2019 Guido Aulisi <guido.aulisi@gmail.com> - 1.6.4-1
- Update to 1.6.4

* Sun Aug 11 2019 Guido Aulisi <guido.aulisi@gmail.com> - 1.6.2-1
- Update to 1.6.2
- Use python3

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jul 15 2018 Guido Aulisi <guido.aulisi@gmail.com> - 1.6.0-7
- Fix FTBFS due to the move of /usr/bin/python into a separate package
- Add BR for gcc and gcc-c++

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 15 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.6.0-5
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Apr 12 2017 Guido Aulisi <guido.aulisi@gmail.com> - 1.6.0-1
- Update to 1.6.0
- Build Qt5 GUI
- Drop deprecated Group tags
- Use hardened LDFLAGS

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.4.6-4
- Rebuilt for GCC 5 C++11 ABI change

* Sun Oct 26 2014 Brendan Jones <brendan.jones.it@gmail.com> 1.4.6-3
- Rebuild for new lv2

* Fri Sep 26 2014 Brendan Jones <brendan.jones.it@gmail.com> 1.4.6-2
- Find correct moc version

* Wed Aug 20 2014 Brendan Jones <brendan.jones.it@gmail.com> 1.4.6-1
- Update to 1.4.6

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Jan 11 2014 Brendan Jones <brendan.jones.it@gmail.com> 1.4.4-1
- Update to 1.4.4

* Sun Aug 25 2013 Brendan Jones <brendan.jones.it@gmail.com> 1.4.2-1
- Update to 1.4.2

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 21 2013 Brendan Jones <brendan.jones.it@gmail.com> 1.4.0-2
- Rebuilt for new LV2 

* Tue May 21 2013 Brendan Jones <brendan.jones.it@gmail.com> 1.4.0-1
- New upstream release

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Dec 15 2012 Brendan Jones <brendan.jones.it@gmail.com> 1.2.0-1
- New upstream release

* Wed Sep 26 2012 Brendan Jones <brendan.jones.it@gmail.com> 1.0.0-5
- Split into framework sub-packages
- Correct package group

* Wed Sep 26 2012 Brendan Jones <brendan.jones.it@gmail.com> 1.0.0-4
- Correct inclusion of missing binaries BZ: 860458

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Apr 22 2012 Brendan Jones <brendan.jones.it@gmail.com> - 1.0.0-2
- Add missing build requires

* Fri Apr 20 2012 Brendan Jones <brendan.jones.it@gmail.com> - 1.0.0-1
- Initial build
