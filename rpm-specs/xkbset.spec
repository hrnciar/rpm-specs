Name:           xkbset
Version:        0.5
Release:        18%{?dist}
Summary:        Tool to configure XKB extensions

License:        BSD
URL:            http://www.math.missouri.edu/~stephen/software/#xkbset
Source0:        http://www.math.missouri.edu/~stephen/software/xkbset/xkbset-%{version}.tar.gz
# 2012-10-03: Sent upstream via e-mail
Source3:        xkbset.desktop
# 2012-10-03: Sent upstream via e-mail
Patch0:         xkbset-0.5-install.patch

# for /usr/include/X11/Xlib.h
BuildRequires: libX11-devel
BuildRequires: desktop-file-utils
BuildRequires: perl-generators
BuildRequires: gcc


%description
xkbset is a program rather like xset in that it allows you to set various
features of the X window interface.  It allows one to configure most of the
options connected with the XKB extensions.  They are described in Section 10 of
XKBlib.ps.

This includes customizing the following:
  MouseKeys:  using the numeric pad keys to move the mouse;
  StickyKeys: where modifiers like control and shift will lock until the
              next key press (good for one finger typing);
  SlowKeys:   The keys will not work unless they are pressed for a certain
              amount of time;
  BounceKeys: If a key is pressed more than once rapidly, only one key
              press will be registered.

%prep
%setup -q
%patch0 -p1 -b .install


%build
make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS"


%install
%make_install X11PREFIX=%{_prefix} INSTALL_PROGRAM=install INSTALL_MAN1=$RPM_BUILD_ROOT/%{_mandir}/man1
desktop-file-install                                    \
--dir=${RPM_BUILD_ROOT}%{_datadir}/applications         \
%{SOURCE3}


%files
%doc COPYRIGHT README TODO VERSIONS
%{_bindir}/xkbset
%{_bindir}/xkbset-gui
%{_mandir}/man1/xkbset.1*
%{_datadir}/applications/xkbset.desktop


%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 16 2018 Till Maas <opensource@till.name> - 0.5-15
- Add missing BR for gcc

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 0.5-4
- Perl 5.18 rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Oct 03 2012 Till Maas <opensource@till.name> - 0.5-2
- Use a patch to fix Makefile
- Do not remove buildroot in %%install
- Add .desktop file

* Tue Oct 02 2012 Till Maas <opensource@till.name> - 0.5-1
- Initial version for Fedora
