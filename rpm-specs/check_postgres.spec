Summary:    PostgreSQL monitoring script
Name:       check_postgres
Version:    2.25.0
Release:    2%{?dist}
License:    BSD
URL:        https://bucardo.org/check_postgres/
BuildArch:  noarch

Source0:    https://github.com/bucardo/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz

Patch0:     0001-Update-doc-and-fix-missing-title-close-tag.patch
Patch1:     0002-Make-sure-our-temp-filehandles-are-doing-UTF-8.patch
Patch2:     0004-Fix-check_replication_slots-on-recently-promoted-ser.patch

BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6.1
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

%description
Script for checking the state of one or more Postgres databases and reporting
back in a Nagios-friendly manner. It is also used for MRTG.

%prep
%autosetup -p1

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}

%if 0%{?rhel} == 7
# When building noarch on Koji you have no guaranteed how _libdir expands:
rm -fr %{buildroot}%{_prefix}/lib*
# Not happening automatically:
sed -i -e 's|^#!/usr/bin/env perl|#!/usr/bin/perl|g' %{buildroot}%{_bindir}/%{name}.pl
%endif

# Fix permissions
chmod 755 %{buildroot}%{_bindir}/%{name}.pl
chmod 644 %{buildroot}%{_mandir}/man1/%{name}.*

# Fix man page filename
mv %{buildroot}%{_mandir}/man1/%{name}.1p %{buildroot}%{_mandir}/man1/%{name}.pl.1

%files
%license LICENSE
%doc %{name}.pl.html README.md TODO
%{_mandir}/man1/%{name}.pl.1*
%{_bindir}/%{name}.pl

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.25.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 02 2020 Simone Caronni <negativo17@gmail.com> - 2.25.0-1
- Update to 2.25.0.
- Add patches from upstream.
- Use autosetup macro.
- rpmlint fixes.
- Trim changelog.
- Use automatic dependency generator.

* Thu May 21 2020 Petr Pisar <ppisar@redhat.com> - 2.24.0-5
- Specify all dependencies
- Package a license
- Align a spec file with the current packaging guide lines
- Fix the file permissions

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 9 2019 Devrim Gündüz <devrim@gunduz.org> - 2.24.0-3
- Attempt to fix FTBFS, and also use more macros.

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 16 2019 Devrim Gündüz <devrim@gunduz.org> - 2.24.0-1
- Update to 2.24.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.22.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.22.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.22.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild
