Name:    freight
Version: 0.3.10
Release: 8%{?dist}
Summary: A modern take on the Debian archive

License: BSD
URL:     https://github.com/freight-team/%{name}
Source0: https://github.com/freight-team/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

Patch1:  freight-0.3.7-libs-usrshare.patch

BuildArch: noarch

Requires: coreutils
Requires: dpkg
Requires: gnupg

%description
freight programs create the files needed to serve a Debian archive. The actual
serving is done via your favorite HTTP server.

%prep
%setup -qn %{name}-%{version}
%patch1 -p1

%build
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} \
             prefix=%{_prefix} \
             bindir=%{_bindir} \
             libdir=%{_datadir} \
             sysconfdir=%{_sysconfdir} \
             mandir=%{_mandir}

mv %{buildroot}%{_sysconfdir}/%{name}.conf{.example,}

# VARLIB, freight library
mkdir -p %{buildroot}%{_sharedstatedir}/%{name}

# VARCACHE, freight cache (to be served by httpd)
mkdir -p %{buildroot}%{_localstatedir}/cache/%{name}

# some empty config files are shipped
find %{buildroot}%{_sysconfdir} -type f -size 0 -delete

%files
%{_bindir}/%{name}*
%{_datadir}/%{name}
%{_localstatedir}/cache/%{name}
%{_sharedstatedir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}.conf
%doc %{_mandir}/man1/*
%doc %{_mandir}/man5/*
%doc LICENSE NOTES README.md

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 22 2016 Dominic Cleal <dominic@cleal.org> - 0.3.10-1
- Update to 0.3.10

* Wed Mar 30 2016 Dominic Cleal <dominic@cleal.org> - 0.3.8-1
- Update to 0.3.8

* Thu Mar 24 2016 Dominic Cleal <dominic@cleal.org> - 0.3.7-1
- Update to 0.3.7

* Wed Mar 09 2016 Dominic Cleal <dominic@cleal.org> - 0.3.6-1
- Update to 0.3.6

* Fri Feb 12 2016 Dominic Cleal <dcleal@redhat.com> - 0.3.5-12
- Fix missing patch call

* Thu Feb 11 2016 Dominic Cleal <dcleal@redhat.com> - 0.3.5-11
- Add patch to fix SHA field labels

* Mon Feb 08 2016 Dominic Cleal <dcleal@redhat.com> - 0.3.5-10
- Change date patch to add Valid-Until field

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb 01 2016 Dominic Cleal <dcleal@redhat.com> - 0.3.5-8
- Add patch to add date to release file

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 04 2015 Dominic Cleal <dcleal@redhat.com> - 0.3.5-6
- Fix more loading of libs from /usr/share

* Thu Jun 04 2015 Dominic Cleal <dcleal@redhat.com> - 0.3.5-5
- Fix loading of libs from /usr/share

* Tue Jul 08 2014 Dominic Cleal <dcleal@redhat.com> - 0.3.5-4
- Remove manual copy of doc files

* Tue Jul 08 2014 Dominic Cleal <dcleal@redhat.com> - 0.3.5-3
- Simplify docs inclusion in files section
- Use install instead of cp to copy documentation
- Fix location of review ticket number

* Mon Jul 07 2014 Dominic Cleal <dcleal@redhat.com> - 0.3.5-2
- Added LICENSE, NOTES and README.md to files section
- Added review ticket number to initial changelog

* Tue Jul 01 2014 Dominic Cleal <dcleal@redhat.com> - 0.3.5-1
- Initial version (#1115049)
