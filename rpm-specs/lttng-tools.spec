%define with_python          0%{!?_without_python:1}

%if %{with_python}
    %define arg_python --enable-python-bindings
%else
    %define arg_python --disable-python-bindings
%endif


Name:           lttng-tools
Version:        2.12.1
Release:        2%{?dist}
License:        GPLv2 and LGPLv2
URL:            http://lttng.org
Summary:        LTTng control and utility programs
Source0:        http://lttng.org/files/lttng-tools/%{name}-%{version}.tar.bz2
Source1:        http://lttng.org/files/lttng-tools/%{name}-%{version}.tar.bz2.asc
# gpg2 --export --export-options export-minimal 7F49314A26E0DE78427680E05F1B2A0789F12B11 > gpgkey-7F49314A26E0DE78427680E05F1B2A0789F12B11.gpg
Source2:        gpgkey-7F49314A26E0DE78427680E05F1B2A0789F12B11.gpg
Source3:        lttng-sessiond.service

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  libxml2-devel >= 2.7.6
BuildRequires:  lttng-ust-devel >= 2.12.0
BuildRequires:  lttng-ust-devel < 2.13.0
BuildRequires:  popt-devel
BuildRequires:  systemd-units
BuildRequires:  systemtap-sdt-devel
BuildRequires:  userspace-rcu-devel >= 0.9.0

# For check
#BuildRequires:  perl-Test-Harness procps-ng
Requires(pre):  shadow-utils
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

#GCC crash when building this package on arm with hardening activated (See bug 987192).
%ifnarch %{arm}
%global _hardened_build 1
%endif

%description
This package provides the unified interface to control both the LTTng kernel
and userspace (UST) tracers.

%package -n %{name}-devel
Summary:        LTTng control and utility library (development files)
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n %{name}-devel
This package provides the development files to
implement trace control in external applications

%if %{with_python}
%package -n python3-lttng
Summary:        Python bindings for LTTng
%{?python_provide:%python_provide python3-lttng}
BuildRequires:  swig
BuildRequires:  python3-devel

%description -n python3-lttng
This package provides Python bindings for LTTng
%endif

%prep
%autosetup -p1

%build
# Reinitialize libtool with the fedora version to remove Rpath
autoreconf -vif
touch doc/man/*.1 doc/man/*.3 doc/man/*.8

%configure \
    --disable-static \
    %{?arg_python}

make %{?_smp_mflags} V=1

%check
#make check

%install
make DESTDIR=%{buildroot} install
rm -vf %{buildroot}%{_libdir}/*.la
rm -vf %{buildroot}%{python3_sitearch}/*.la
install -D -m644 %{SOURCE1} %{buildroot}%{_unitdir}/lttng-sessiond.service
# Install upstream bash auto completion for lttng
install -D -m644 extras/lttng-bash_completion %{buildroot}%{_sysconfdir}/bash_completion.d/lttng

%pre
getent group tracing >/dev/null || groupadd -r tracing
exit 0

%post
/sbin/ldconfig
%systemd_post lttng-sessiond.service

%preun
%systemd_preun lttng-sessiond.service

%postun
/sbin/ldconfig
%systemd_postun_with_restart lttng-sessiond.service 

%files
%dir %{_libdir}/lttng
%dir %{_libdir}/lttng/libexec
%{_bindir}/lttng
%{_bindir}/lttng-crash
%{_bindir}/lttng-sessiond
%{_bindir}/lttng-relayd
%{_libdir}/lttng/libexec/lttng-consumerd
%{_libdir}/*.so.*
%{_mandir}/man1/lttng.1.gz
%{_mandir}/man1/lttng-add-context.1.gz
%{_mandir}/man1/lttng-clear.1.gz
%{_mandir}/man1/lttng-crash.1.gz
%{_mandir}/man1/lttng-create.1.gz
%{_mandir}/man1/lttng-destroy.1.gz
%{_mandir}/man1/lttng-disable-channel.1.gz
%{_mandir}/man1/lttng-disable-event.1.gz
%{_mandir}/man1/lttng-disable-rotation.1.gz
%{_mandir}/man1/lttng-enable-channel.1.gz
%{_mandir}/man1/lttng-enable-event.1.gz
%{_mandir}/man1/lttng-enable-rotation.1.gz
%{_mandir}/man1/lttng-help.1.gz
%{_mandir}/man1/lttng-list.1.gz
%{_mandir}/man1/lttng-load.1.gz
%{_mandir}/man1/lttng-metadata.1.gz
%{_mandir}/man1/lttng-regenerate.1.gz
%{_mandir}/man1/lttng-rotate.1.gz
%{_mandir}/man1/lttng-save.1.gz
%{_mandir}/man1/lttng-set-session.1.gz
%{_mandir}/man1/lttng-snapshot.1.gz
%{_mandir}/man1/lttng-start.1.gz
%{_mandir}/man1/lttng-status.1.gz
%{_mandir}/man1/lttng-stop.1.gz
%{_mandir}/man1/lttng-track.1.gz
%{_mandir}/man1/lttng-untrack.1.gz
%{_mandir}/man1/lttng-version.1.gz
%{_mandir}/man1/lttng-view.1.gz
%{_mandir}/man8/lttng-relayd.8.gz
%{_mandir}/man8/lttng-sessiond.8.gz
%{_defaultdocdir}/%{name}/LICENSE
%{_defaultdocdir}/%{name}/README.md
%{_defaultdocdir}/%{name}/ChangeLog
%{_defaultdocdir}/%{name}/live-reading-howto.txt
%{_defaultdocdir}/%{name}/python-howto.txt
%{_defaultdocdir}/%{name}/quickstart.txt
%{_defaultdocdir}/%{name}/snapshot-howto.txt
%{_defaultdocdir}/%{name}/streaming-howto.txt
%{_unitdir}/lttng-sessiond.service
%{_sysconfdir}/bash_completion.d/
%{_datadir}/xml/lttng/session.xsd

%files -n %{name}-devel
%{_mandir}/man3/lttng-health-check.3.gz
%{_defaultdocdir}/%{name}/live-reading-protocol.txt
%{_defaultdocdir}/%{name}/valgrind-howto.txt
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/lttng-ctl.pc

%if %{with_python}
%files -n python%{python3_pkgversion}-lttng
%{_defaultdocdir}/%{name}/python-howto.txt
%{python3_sitelib}/lttng.py
%{python3_sitelib}/__pycache__/*.pyc
%{python3_sitearch}/_lttng.so*
%endif

%changelog
* Wed May 27 2020 Miro Hrončok <mhroncok@redhat.com> - 2.12.1-2
- Rebuilt for Python 3.9

* Tue May 26 2020 Michael Jeanson <mjeanson@efficios.com> - 2.12.1-1
- New upstream release

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.12.0-2
- Rebuilt for Python 3.9

* Tue Apr 14 2020 Michael Jeanson <mjeanson@efficios.com> - 2.12.0-1
- New upstream release

* Wed Feb 12 2020 Michael Jeanson <mjeanson@efficios.com> - 2.11.1-2
- Fix session rotation with kernel domain

* Fri Feb 07 2020 Michael Jeanson <mjeanson@efficios.com> - 2.11.1-1
- New upstream release
- Re-enable python subpackage
- Add buildep on systemtap-sdt-devel

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 22 2020 Michael Jeanson <mjeanson@efficios.com> - 2.11.0-2
- Add patch to fix build failure with GCC 10

* Tue Oct 22 2019 Michael Jeanson <mjeanson@efficios.com> - 2.11.0-1
- New upstream release
- Disable python subpackage until swig is fixed

* Mon Oct 21 2019 Scott K Logan <logans@cottsay.net> - 2.10.7-3
- Add python subpackage

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 03 2019 Michael Jeanson <mjeanson@efficios.com> - 2.10.7-1
- New upstream release

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 24 2018 Michael Jeanson <mjeanson@efficios.com> - 2.10.5-1
- New upstream release

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue May 29 2018 Michael Jeanson <mjeanson@efficios.com> - 2.10.4-1
- New upstream release

* Tue Mar 27 2018 Michael Jeanson <mjeanson@efficios.com> - 2.10.3-1
- New upstream release

* Tue Feb 13 2018 Michael Jeanson <mjeanson@efficios.com> - 2.10.2-1
- New upstream release

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Michael Jeanson <mjeanson@efficios.com> - 2.10.1-1
- New upstream release

* Thu Aug 17 2017 Dan Horák <dan[at]danny.cz> - 2.10.0-2
- drop the s390(x) build workaround

* Wed Aug 02 2017 Michael Jeanson <mjeanson@efficios.com> - 2.10.0-1
- New upstream release

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 22 2017 Michael Jeanson <mjeanson@efficios.com> - 2.9.5-1
- New upstream release

* Wed Mar 01 2017 Michael Jeanson <mjeanson@efficios.com> - 2.9.4-1
- New upstream release

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 09 2017 Michael Jeanson <mjeanson@efficios.com> - 2.9.3-1
- New upstream release

* Thu Dec 01 2016 Michael Jeanson <mjeanson@efficios.com> - 2.9.0-1
- New upstream release
- Drop asciidoc and xmlto from build deps

* Tue Oct 11 2016 Michael Jeanson <mjeanson@efficios.com> - 2.8.2-1
- New upstream release
- Add asciidoc and xmlto to build deps

* Fri Aug 05 2016 Michael Jeanson <mjeanson@efficios.com> - 2.8.1-1
- New upstream release

* Wed Jun 22 2016 Michael Jeanson <mjeanson@efficios.com> - 2.8.0-1
- New upstream release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jul 23 2015 Michael Jeanson <mjeanson@gmail.com> - 2.6.0-1
- New upstream release
- Add mi string declaration as extern patch

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Nov 03 2014 Suchakra Sharma <suchakra@fedoraproject.org> - 2.5.1-1
- New upstream release
- Update URL
- Update some BuildRequires
- Add session.xsd file to package

* Tue Oct 21 2014 Dan Horák <dan[at]danny.cz> - 2.4.1-4
- add build workaround for s390(x)

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 20 2014 Yannick Brosseau <yannick.brosseau@gmail.com> - 2.4.1-1
- New upstream release

* Sat Feb 22 2014 Yannick Brosseau <yannick.brosseau@gmail.com> - 2.3.0-3
- Rebuilt for URCU soname bump

* Tue Sep 24 2013 Yannick Brosseau <yannick.brosseau@gmail.com> - 2.3.0-2
- Disable hardening flags on arm, since it does not build with them

* Fri Sep 20 2013 Yannick Brosseau <yannick.brosseau@gmail.com> - 2.3.0-1
- New upstream release

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 23 2013 Yannick Brosseau <yannick.brosseau@gmail.com> - 2.2.3-1
- New upstream bugfix version

* Mon Jul 22 2013 Yannick Brosseau <yannick.brosseau@gmail.com> - 2.2.2-1
- New upstream bugfix version

* Tue Jul 16 2013 Yannick Brosseau <yannick.brosseau@gmail.com> - 2.2.1-1
- New upstream version

* Fri May 17 2013 Yannick Brosseau <yannick.brosseau@gmail.com> - 2.1.1-2
- Add hardening option (#955452)
- Use new systemd-rpm macros (#850195)

* Tue Feb 26 2013 Yannick Brosseau <yannick.brosseau@gmail.com> - 2.1.1-1
- New upstream version

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Oct 23 2012 Yannick Brosseau <yannick.brosseau@gmail.com> - 2.0.4-1
- New upstream version

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jul 07 2012 Yannick Brosseau <yannick.brosseau@gmail.com> - 2.0.3-1
- New upstream version and updates from review comments 

* Tue Jun 19 2012 Yannick Brosseau <yannick.brosseau@gmail.com> - 2.0.2-1
- New package, inspired by the one from OpenSuse

