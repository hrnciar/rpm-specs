Name:           abi-tracker
Version:        1.11
Release:        9%{?dist}
Summary:        Tool to visualize ABI changes timeline of a C/C++ library

License:        GPL+ and LGPLv2+
URL:            https://github.com/lvc/abi-tracker
Source0:        https://github.com/lvc/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  perl%{?fedora:-interpreter}
BuildRequires:  perl-generators
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Find)
# Needed to run abi-tracker to generate man page.
BuildRequires:  help2man
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(strict)


Requires:       abi-dumper >= 0.99.16
Requires:       vtable-dumper >= 1.1
Requires:       abi-compliance-checker >= 1.99.21
Requires:       pkgdiff >= 1.6.4
Requires:       rfcdiff >= 1.41
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:       elfutils


%description
A tool to visualize ABI changes timeline of a C/C++ software library.
  
The tool requires the input profile of the library in JSON format. It can be
created manually or automatically generated by the ABI Monitor:
https://github.com/lvc/abi-monitor


%prep
%setup -q


%build
# Nothing to build


%install
mkdir -p %{buildroot}%{_prefix}
perl Makefile.pl -install --prefix=%{_prefix} --destdir=%{buildroot}
%{_fixperms} %{buildroot}/*

# Create man page
mkdir -p %{buildroot}%{_mandir}/man1
help2man -s 1 -N --version-string %{version} \
    %{buildroot}%{_bindir}/%{name} > %{buildroot}%{_mandir}/man1/%{name}.1


%files
%license LICENSE
%doc HOWTO README
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_mandir}/man1/%{name}.1*


%changelog
* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.11-9
- Perl 5.32 rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.11-6
- Perl 5.30 rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.11-3
- Perl 5.28 rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 30 2017 Richard Shaw <hobbes1069@gmail.com> - 1.11-1
- Update to latest upstream release.

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 06 2017 Richard Shaw <hobbes1069@gmail.com> - 1.10-1
- Update to latest upstream release.

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.9-3
- Perl 5.26 rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Oct 13 2016 Richard Shaw <hobbes1069@gmail.com> - 1.9-1
- Update to latest upstream release.

* Wed Jul  6 2016 Richard Shaw <hobbes1069@gmail.com> - 1.8-1
- Update to latest upstream release.

* Wed Jun  1 2016 Richard Shaw <hobbes1069@gmail.com> - 1.7-1
- Update to latest upstream release.

* Thu May 19 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.6-2
- Perl 5.24 re-rebuild of bootstrapped packages

* Sun May 15 2016 Richard Shaw <hobbes1069@gmail.com> - 1.6-1
- Update to latest upstream release.

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.5-2
- Perl 5.24 rebuild

* Sun Mar 13 2016 Richard Shaw <hobbes1069@gmail.com> - 1.5-1
- Update to latest upstream release.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec  7 2015 Richard Shaw <hobbes1069@gmail.com> - 1.4-2
- Add manpage via help2man.
- Query upstream to clarify licensing.
  https://github.com/lvc/abi-tracker/issues/1

* Sun Dec  6 2015 Richard Shaw <hobbes1069@gmail.com> - 1.4-1
- Initial packaging.
- 