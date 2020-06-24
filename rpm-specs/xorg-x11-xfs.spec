%global uid 43
%global username xfs

# Component versions
%global xfsinfo 1.0.5
%global fslsfonts 1.0.5
%global fstobdf 1.0.6
%global showfont 1.0.5

Summary:    X.Org X11 xfs font server
Name:       xorg-x11-xfs
Version:    1.2.0
Release:    7%{?dist}
Epoch:      1
License:    MIT
URL:        http://www.x.org

Source0:    https://www.x.org/pub/individual/app/xfs-%{version}.tar.bz2
Source1:    https://www.x.org/pub/individual/app/xfsinfo-%{xfsinfo}.tar.bz2
Source2:    https://www.x.org/pub/individual/app/fslsfonts-%{fslsfonts}.tar.bz2
Source3:    https://www.x.org/pub/individual/app/fstobdf-%{fstobdf}.tar.bz2
Source4:    https://www.x.org/pub/individual/app/showfont-%{showfont}.tar.bz2
Source10:   xfs.service
Source11:   xfs.init
Source12:   xfs.config
Source13:   xfs.tmpfiles

BuildRequires:  font-util >= 1.1
BuildRequires:  libtool
BuildRequires:  pkgconfig(libfs)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xfont2) >= 2.0
BuildRequires:  pkgconfig(xorg-macros)
BuildRequires:  pkgconfig(xtrans)
BuildRequires: systemd

Provides:   xfs = %{version}

Requires(pre):  shadow-utils

Requires(post):    systemd
Requires(preun):   systemd
Requires(postun):  systemd

%description
X.Org X11 xfs font server.

%package utils
Summary:    X.Org X11 font server utilities
Provides:   xfsinfo = %{xfsinfo}
Provides:   fslsfonts = %{fslsfonts}
Provides:   fslsfonts = %{fslsfonts}
Provides:   fstobdf = %{fstobdf}
Provides:   showfont = %{showfont}
#Requires: %{name} = %{version}-%{release}

%description utils
X.Org X11 font server utilities.

%prep
%setup -q -c %{name}-%{version} -a1 -a2 -a3 -a4

%build

# Build all apps
{
   for app in * ; do
      pushd $app
      autoreconf -vif
      %configure
      make %{?_smp_mflags}
      popd
   done
}

%install
# Install all apps
{
   for app in * ; do
      pushd $app
      %make_install
      popd
   done
}

# Install the Red Hat xfs config file and initscript
install -D -p -m 644 %{SOURCE12} $RPM_BUILD_ROOT%{_sysconfdir}/X11/fs/config

# Systemd unit files
mkdir -p %{buildroot}%{_unitdir}
install -p -m 644 -D %{SOURCE10} %{buildroot}%{_unitdir}/xfs.service
install -p -m 644 -D %{SOURCE13} %{buildroot}%{_tmpfilesdir}/xfs.conf

%pre
getent group %username >/dev/null || groupadd -g %uid -r %username &>/dev/null || :
getent passwd %username >/dev/null || useradd -u %uid -r -s /sbin/nologin \
    -d %{_sysconfdir}/X11/fs -M -c 'X Font Server' -g %username %username &>/dev/null || :
exit 0

%post
%systemd_post xfs.service

%preun
%systemd_preun xfs.service

%postun
%systemd_postun_with_restart xfs.service

%files
%doc xfs-%{version}/COPYING
%{_bindir}/xfs
%dir %{_sysconfdir}/X11/fs
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/X11/fs/config
%{_mandir}/man1/xfs.1*
%{_unitdir}/xfs.service
%{_tmpfilesdir}/xfs.conf

%files utils
%doc xfs-%{version}/COPYING
%{_bindir}/fslsfonts
%{_bindir}/fstobdf
%{_bindir}/showfont
%{_bindir}/xfsinfo
%{_mandir}/man1/fslsfonts.1*
%{_mandir}/man1/fstobdf.1*
%{_mandir}/man1/showfont.1*
%{_mandir}/man1/xfsinfo.1*

%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Mar 21 2019 Adam Jackson <ajax@redhat.com> - 1.2.0-5
- Rebuild for xtrans 1.4.0

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Nov 28 2017 Adam Jackson <ajax@redhat.com> - 1.2.0-1
- xfs 1.2.0
- General specfile cleanup

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.1.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Apr 25 2017 Adam Jackson <ajax@redhat.com> - 1.1.4-6
- Move virtual provides for !xfs to the -xfs-utils subpackage where they belong

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 20 2016 Peter Hutterer <peter.hutterer@redhat.com>
- s/define/global/

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jan 08 2015 Simone Caronni <negativo17@gmail.com> - 1:1.1.4-2
- Clean up SPEC file, fix rpmlint warnings.
- Rewrite completely init script and install logic completely according to
  packaging guidelines.
- Add systemd files (starting Fedora 22 / RHEL 8).
- Remove upgrade stuff (~2005/2006).
- xfsinfo 1.0.5
- fslsfonts 1.0.5
- fstobdf 1.0.6
- showfont 1.0.5

* Thu Aug 28 2014 Hans de Goede <hdegoede@redhat.com> - 1:1.1.4-1
- xfs 1.1.4 (rhbz#952216)
- xfsinfo 1.0.4
- fslsfonts 1.0.4
- fstobdf 1.0.5
- showfont 1.0.4

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jun 09 2014 Adam Jackson <ajax@redhat.com> 1.1.3-1
- xfs 1.1.3 plus new fontproto compat
- Pre-F12 changelog trim

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Mar 23 2012 Adam Jackson <ajax@redhat.com> 1.1.2-1
- xfs 1.1.2
