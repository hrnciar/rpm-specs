%global commit 89c264d18326248cf614377b74b9b002a7a9f28f
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%global iipver 1.1

Name:           iipsrv
Version:        1.1.0
Release:        2.0%{?dist}
Summary:        Light-weight streaming for viewing and zooming of ultra high-resolution images

License:        GPLv3+
URL:            http://iipimage.sourceforge.net
Source0:        https://github.com/ruven/%{name}/archive/%{name}-%{iipver}.tar.gz
Source1:        %{name}-httpd.conf
Source2:        README.rpm
Source3:        %{name}-logrotate
Source10:       %{name}.service
Patch0:         %{name}-remove-bundled-fcgi.patch

BuildRequires:  gcc-c++
BuildRequires:  zlib-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libtiff-devel
BuildRequires:  fcgi-devel
BuildRequires:  lcms2-devel
BuildRequires:  libpng-devel
BuildRequires:  openjpeg2-devel
%if 0%{?fedora}
BuildRequires:  libmemcached-devel
%endif
BuildRequires:  systemd
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  selinux-policy-devel
BuildRequires:  checkpolicy

Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
Requires:       %{_sysconfdir}/logrotate.d

Requires(post):   /sbin/restorecon
Requires(post):   /usr/sbin/semanage
Requires(postun): /usr/sbin/semanage


%description
Light-weight streaming client-server system for the web-based viewing and
zooming of ultra high-resolution images. It is designed to be bandwidth
and memory efficient and usable even over a slow internet connection.

The system can handle both 8 and 16 bit images, CIELAB colorimetric images and
scientific imagery such as multispectral images. The fast streaming is
tile-based meaning the client only needs to download the portion of the whole
image that is visible on the screen of the user at their current viewing
resolution and not the entire image.
This makes it possible to view, navigate and zoom in real-time around
multi-gigapixel size images that would be impossible to download and
manipulate on the local machine. It also makes the system very scalable as
the number of image tile downloads will remain the same regardless of the
size of the source image. In addition, to reduce the bandwidth necessary even
further, the tiles sent back are dynamically JPEG compressed with a level of
compression that can be optimized for the available bandwidth by the client.


%package httpd-fcgi
Summary:         Apache HTTPD files for %{name}
Requires:        %{name} = %{version}-%{release}
Requires:        httpd
Requires:        mod_fcgid
Requires(post):  systemd
BuildArch:       noarch


%description httpd-fcgi
IIPImage server Apache/mod_fcgid files


%prep
%setup -q -n %{name}-%{name}-%{iipver}
%patch0 -p1
#fix man
sed -e "s/\.Iiipsrv/.I iipsrv/" -i man/%{name}.8
#specfific fixes for el5...
%if 0%{?rhel}  == 5
sed 's/AC_PROG_MAKE_SET/AC_PROG_MAKE_SET\
AC_PROG_RANLIB/' -i configure.in
mkdir m4
%endif
#remove bundled lib
%if 0%{?rhel}  == 5
#directives names has changed since pre ASF releases of mod_fcgid
#see http://httpd.apache.org/mod_fcgid/mod/mod_fcgid.html#upgrade
sed -i \
  -e 's/FcgidIdleTimeout/IdleTimeout/' \
  -e 's/FcgidMaxProcessesPerClass/DefaultMaxClassProcessCount/' \
  %{SOURCE1}
%endif


%build
./autogen.sh
%configure --with-fcgi-lib=%{_includedir}
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.d/
install -m 0644 -D -p %{SOURCE1} ${RPM_BUILD_ROOT}%{_sysconfdir}/httpd/conf.d/%{name}.conf

mkdir -p $RPM_BUILD_ROOT%{_libexecdir}/%{name}
install -m 0755 -D -p src/iipsrv.fcgi $RPM_BUILD_ROOT%{_libexecdir}/%{name}/%{name}.fcgi

cp %{SOURCE2} .

#systemd stuff
mkdir -p $RPM_BUILD_ROOT%{_unitdir}
install -p -m 644 %{SOURCE10} $RPM_BUILD_ROOT%{_unitdir}/%{name}.service

#log stuff
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/log/%{name}
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d
install -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/%{name}



%post httpd-fcgi
(
# File context
semanage fcontext -a -s system_u -t httpd_log_t -r s0 "%{_localstatedir}/log/%{name}(/.*)?"
# files created by app
restorecon -R %{_localstatedir}/log/%{name}
) &>/dev/null

/bin/systemctl condrestart httpd.service

%pre
%{_sbindir}/useradd -r -s /sbin/nologin %{name} 2> /dev/null || :

%preun
%systemd_preun %{name}.service

%post
%systemd_post %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%postun httpd-fcgi
if [ "$1" -eq "0" ]; then
    # Remove the File Context
    (
    semanage fcontext -d "%{_localstatedir}/log/%{name}(/.*)?"
    ) &>/dev/null
fi
/bin/systemctl condrestart httpd.service


%files
%license COPYING
%doc README AUTHORS ChangeLog TODO doc/* README.rpm
%{_libexecdir}/%{name}/%{name}.fcgi
%{_unitdir}/%{name}.service
%{_mandir}/man8/%{name}.8.gz
%dir %{_localstatedir}/log/%{name}
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}


%files httpd-fcgi
%config(noreplace) %{_sysconfdir}/httpd/conf.d/%{name}.conf


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2.0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Sep 28 2019 Johan Cwiklinski <johan AT x-tnd DOT be> - 1.1-1.0
- Update to 1.1, add openjpeg2 support

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-14.0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-13.0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Nov 18 2018 Peter Robinson <pbrobinson@fedoraproject.org> 1.0.0-12.0
- Drop old release conditionals and sysv migration bits
- Use %%license

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-11.0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-10.0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-9.0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-8.0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-7.0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu May 05 2016 Johan Cwiklinski <johan AT x-tnd DOT be> - 1.0.0-6.0
- Update to final 1.0 release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5.0.git2431b45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-4.0.git2431b45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.0.0-3.0.git2431b45
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2.0.git2431b45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 13 2014 Johan Cwiklinski <johan AT x-tnd DOT be> - 1.0.0-1.0.git2431b45
- Update to latest git commit
- Add specific log directory and logrotate stuff
- Change default VERBOSITY, JPEG_QUALITY to better values
- Set SELinux contexts for log files when installing httpd-fcgi subpackage

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-0.9.git0b63de7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-0.8.git0b63de7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri May 24 2013 Johan Cwiklinski <johan AT x-tnd DOT be> - 1.0.0-0.7.git0b63de7
- Fix license
- Set httpd-fcgi sub-package noarch (exept for EL5)
- Add missing BuilRequires
- Fix unconsistent scriplets
- Add missing SysV postun
- Add missing SysV Requires
- Add comment on service file on how to tune
- Add missing Requires on httpd-fcgi subpackage
- Remove bundled lib
- New mod_fcgid directives names (except for el5)

* Wed May 22 2013 Johan Cwiklinski <johan AT x-tnd DOT be> - 1.0.0-0.6.git0b63de7
- Systemd configuration directives are now handled in unit file

* Sun May 19 2013 Johan Cwiklinski <johan AT x-tnd DOT be> - 1.0.0-0.5.git0b63de7
- Add SysV service files

* Sun May 19 2013 Johan Cwiklinski <johan AT x-tnd DOT be> - 1.0.0-0.4.git0b63de7
- Add iipsrv systemd service and user
- Remove Requires on mod_fcgi
- Fix service name for non fedora

* Sun May 19 2013 Johan Cwiklinski <johan AT x-tnd DOT be> - 1.0.0-0.3.git0b63de7
- Remove strip and reactivate debuginfo package
- Use system fcgi and not bundeld one, remove -devel subpackage
- Do not install stuff in /var/www
- Create httpd-fcgi subpackage

* Sat May 18 2013 Johan Cwiklinski <johan AT x-tnd DOT be> - 1.0.0-0.2.git0b63de7
- Specfile cleanup
- Replace %%define by %%global

* Sun May 05 2013 Johan  Cwiklinski <johan AT x-tnd DOT be> - 1.0.0-0.1.git0b63de7
- Rebuild from latest GIT snapshot

* Thu Apr 21 2011 Johan Cwiklinski <johan AT x-tnd DOT be> - 0.9.9-3.trashy
- memcached support (for Fedora only, does not compile on EL 5/6)

* Wed Apr 20 2011 Johan Cwiklinski <johan AT x-tnd DOT be> - 0.9.9-2.trashy
- Upgrade to 0.9.9

* Sat Jul 24 2010 Johan Cwiklinski <johan AT x-tnd DOT be> - 0.9.9-1.20100724
- Upgrade to latest SVN

* Wed Dec 23 2009 Johan Cwiklinski <johan AT x-tnd DOT be> - 0.9.9-1.20091202
- Upgrade to latest SVN

* Wed Dec 23 2009 Johan Cwiklinski <johan AT x-tnd DOT be> - 0.9.8-1.20090722
- Rebuild for F-12

* Mon Mar 30 2009 Johan Cwiklinski <johan AT x-tnd DOT be> - 0.9.8-1.20090331
- Initial packaging
