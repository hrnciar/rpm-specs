Name:           sidplayfp
Version:        2.0.2
Release:        1%{?dist}
Summary:        SID chip music module player
License:        GPLv2+
URL:            http://sourceforge.net/projects/sidplay-residfp/
Source0:        http://downloads.sourceforge.net/sidplay-residfp/%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  libsidplayfp-devel >= 2.0
BuildRequires:  alsa-lib-devel pulseaudio-libs-devel libtool

%description
A player for playing SID music modules originally created on the Commodore 64
and compatibles.


%prep
%setup -q
# Regenerate autofoo stuff, it is better to always build this from source
rm -r aclocal.m4 build-aux
autoreconf -ivf


%build
%configure
make %{?_smp_mflags}


%install
%make_install


%files
%doc AUTHORS README
%license COPYING
%{_bindir}/sidplayfp
%{_bindir}/stilview
%{_mandir}/man?/sidplayfp.*
%{_mandir}/man1/stilview.1*


%changelog
* Thu Apr 30 2020 Hans de Goede <hdegoede@redhat.com> - 2.0.2-1
- Update to 2.0.2

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 09 2019 Karel Volný <kvolny@redhat.com> - 2.0.1-1
- Update to 2.0.1

* Sat Aug 31 2019 Hans de Goede <hdegoede@redhat.com> - 2.0.0-1
- Update to 2.0.0 upstream release

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 30 2018 Hans de Goede <hdegoede@redhat.com> - 1.4.4-1
- Update to 1.4.4

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jul 10 2015 Hans de Goede <hdegoede@redhat.com> - 1.4.0-1
- Update to 1.4.0

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.3.0-4
- Rebuilt for GCC 5 C++11 ABI change

* Fri Feb 20 2015 Michael Schwendt <mschwendt@fedoraproject.org> - 1.3.0-3
- Rebuild for GCC 5 rebuilt libsidplayfp.

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Aug 12 2014 Hans de Goede <hdegoede@redhat.com> - 1.3.0-1
- New upstream release 1.3.0

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Apr  6 2014 Hans de Goede <hdegoede@redhat.com> - 1.2.0-1
- New upstream release 1.2.0
- Drop our patches (merged upstream)

* Mon Sep 30 2013 Hans de Goede <hdegoede@redhat.com> - 1.1.0-1
- New upstream release 1.1.0
- Drop our patches (merged upstream)

* Wed Aug 21 2013 Hans de Goede <hdegoede@redhat.com> - 1.0.3-1
- New upstream release 1.0.3

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Apr 11 2013 Hans de Goede <hdegoede@redhat.com> - 1.0.1-1
- Initial RPM packaging for Fedora
