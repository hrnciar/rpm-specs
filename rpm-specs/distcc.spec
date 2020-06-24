%define _hardened_build 1

Name:       distcc
Version:    3.3.3
Release:    6%{?dist}
Summary:    Distributed C/C++ compilation
License:    GPLv2+
URL:        https://github.com/distcc/distcc
Source0:    https://github.com/distcc/distcc/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:    hosts.sample
Source2:    distccd.service
Patch0:     distcc-localhost.patch

BuildRequires: automake
BuildRequires: autoconf
BuildRequires: libtool
BuildRequires: popt-devel
BuildRequires: libgnomeui-devel
BuildRequires: pango-devel
BuildRequires: python3-devel
BuildRequires: desktop-file-utils
BuildRequires: avahi-devel
BuildRequires: krb5-devel
BuildRequires: binutils-devel

%description
distcc is a program to distribute compilation of C or C++ code across
several machines on a network. distcc should always generate the same
results as a local compile, is simple to install and use, and is often
two or more times faster than a local compile.


%package    gnome
Summary:    Gnome frontend of distcc monitoring tool
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description gnome
This package contains the Gnome frontend of the distcc monitoring tool.


%package     server
Summary:    Server for distributed C/C++ compilation
License:    GPLv2+

Requires:   %{name}%{?_isa} = %{version}-%{release}
Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units
Requires(post): systemd-sysv

%description server
This package contains the compilation server needed to use %{name}.


%prep
%setup -q
%patch0 -p0

%build
export PYTHON='/usr/bin/python3'
./autogen.sh
export CFLAGS="%{optflags} -fcommon"
%configure --with-gnome --disable-Werror --with-auth
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT

# Move desktop file to right directory
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
mv $RPM_BUILD_ROOT%{_datadir}/%{name}/*.desktop $RPM_BUILD_ROOT%{_datadir}/applications/
sed -i 's@Icon=@Icon=%{_datadir}/%{name}/@' $RPM_BUILD_ROOT%{_datadir}/applications/*.desktop

# Install sample hosts file
install -Dm 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/hosts

# Install sample distccd config file
install -Dm 0644 contrib/redhat/sysconfig $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/distccd

# Install distcdd unit file
mkdir -p $RPM_BUILD_ROOT%{_unitdir}
install -Dm 0644 %{SOURCE2} $RPM_BUILD_ROOT%{_unitdir}/distccd.service

# Install distcc dirs
mkdir -p $RPM_BUILD_ROOT/usr/lib/distcc
mkdir -p $RPM_BUILD_ROOT/usr/lib/gcc-cross
if [ ! -d $RPM_BUILD_ROOT/usr/lib64 ]; then
  mkdir -p $RPM_BUILD_ROOT/usr/lib64
fi
ln -s /usr/lib/distcc $RPM_BUILD_ROOT/usr/lib64/distcc

rm -rf $RPM_BUILD_ROOT%{_docdir}/*

%post server
#[ $1 -lt 2 ] && /sbin/chkconfig --add distccd ||:
if [ $1 -eq 1 ] ; then 
    # Initial installation 
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi
%{_sbindir}/update-distcc-symlinks

%preun server
#[ $1 -eq 0 ] && /sbin/chkconfig --del distccd ||:
if [ $1 -eq 0 ] ; then
    # Package removal, not upgrade
    /bin/systemctl --no-reload disable distccd.service > /dev/null 2>&1 || :
    /bin/systemctl stop distccd.service > /dev/null 2>&1 || :
fi

%postun server
/bin/systemctl daemon-reload >/dev/null 2>&1 || :
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    /bin/systemctl try-restart distccd.service >/dev/null 2>&1 || :
fi

%files
%doc AUTHORS doc/* NEWS README.pump TODO
%doc COPYING INSTALL README survey.txt
%{_bindir}/distcc
%{_bindir}/distccmon-text
%{_bindir}/lsdistcc
%{_bindir}/pump
%{_mandir}/man1/distcc.*
%{_mandir}/man1/distccmon*
%{_mandir}/man1/pump*
%{_mandir}/man1/include_server*
%{_mandir}/man1/lsdistcc*
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/hosts
%{python3_sitearch}/include_server*


%files gnome
%{_bindir}/distccmon-gnome
%{_datadir}/%{name}
%{_datadir}/applications/*.desktop


%files server
%doc COPYING README
%{_bindir}/distccd
%{_unitdir}/*
%{_sysconfdir}/default/distcc
%{_sysconfdir}/distcc/*allow*
%{_mandir}/man1/distccd*
%config(noreplace) %{_sysconfdir}/sysconfig/distccd
%{_sbindir}/update-distcc-symlinks
%dir /usr/lib/distcc
/usr/lib64/distcc
%dir /usr/lib/gcc-cross

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.3.3-6
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Gwyn Ciesla <gwync@protonmail.com> - 3.3.3-5
- Build with -fcommon for gcc10.

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.3.3-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.3.3-2
- Rebuilt for Python 3.8

* Thu Aug 15 2019 Gwyn Ciesla <gwync@protonmail.com> - 3.3.3-1
- 3.3.3

* Tue Aug 06 2019 Gwyn Ciesla <gwync@protonmail.com> - 3.3.2-1
- Python 3.

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2rc1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 07 2019 Gwyn Ciesla <gwync@protonmail.com> - 3.2rc1-23
- Honor clients.allow

* Thu Feb 21 2019 Gwyn Ciesla <gwync@protonmail.com> - 3.2rc1-22
- Restrict to localhost by default.

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2rc1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2rc1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Mar 13 2018 Iryna Shcherbina <ishcherb@redhat.com> - 3.2rc1-19
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2rc1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Dec 21 2017 Gwyn Ciesla <limburgher@gmail.com> - 3.2rc1-17
- Drop --verbose, BZ 1523785.

* Thu Dec 21 2017 Gwyn Ciesla <limburgher@gmail.com> - 3.2rc1-16
- Patch for argument bug, BZ 1527368
- Move required components for pump to client package, BZ 1525851

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2rc1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2rc1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2rc1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2rc1-12
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.2rc1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2rc1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 12 2015 Jon Ciesla <limburgher@gmail.com> - 3.2rc1-9
- Enable authentication support, BZ 1201039.

* Wed Aug 20 2014 Andy Grover <agrover@redhat.com> - 3.2rc1-8
- Add patch distcc-minilzo-2.08.patch, to fix CVE-2014-4607 (BZ 1131791)

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2rc1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2rc1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Aug 08 2013 Jon Ciesla <limburgher@gmail.com> - 3.2rc1-5
- Fixed unversioned docdir issue, BZ 993722.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2rc1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu May 16 2013 Jon Ciesla <limburgher@gmail.com> - 3.2rc1-3
- chmod -x .service, BZ 963912

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2rc1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Oct 25 2012 Jon Ciesla <limburgher@gmail.com> - 3.2rc1-1
- Latest upstream, BZ 870200.

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Apr 13 2012 Jon Ciesla <limburgher@gmail.com> - 3.1-6
- Add hardened build.

* Tue Jan 31 2012 Jon Ciesla <limburgher@gmail.com> - 3.1-5
- Migrate to systemd, BZ 770409.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Nov 10 2011 Jon Ciesla <limb@jcomserv.net> - 3.1-3
- Rebuild for libpng 1.5.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Oct 07 2010 Jon Ciesla <limb@jcomserv.net> - 3.1-1
- New upstream, BZ 641032.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.18.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.18.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 22 2008 Denis Leroy <denis@poolshark.org> - 2.18.3-4
- Added Avahi support patch from Lennart

* Tue Feb 19 2008 Denis Leroy <denis@poolshark.org> - 2.18.3-3
- LSB header for init script

* Mon Feb 18 2008 Denis Leroy <denis@poolshark.org> - 2.18.3-2
- Fixed Source0 URL, fixed init script

* Mon Feb  4 2008 Denis Leroy <denis@poolshark.org> - 2.18.3-1
- First version

