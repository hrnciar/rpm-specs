Name:           git-cal
Version:        0.9.1
Release:        15%{?dist}
Summary:        GitHub-like contributions calendar on terminal
License:        MIT
URL:            https://github.com/k4rthik/git-cal

Source0:        https://github.com/k4rthik/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  /usr/bin/pod2man
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
Requires:       perl-interpreter
Requires:       perl(Data::Dumper)
Requires:       perl(Getopt::Long)
Requires:       perl(Pod::Usage)
Requires:       perl(Time::Local)

%description
git-cal is a simple script to view commits calendar (similar to GitHub
contributions calendar) on command line.

%prep
%setup -q

%build
perl Makefile.PL DESTDIR=%{buildroot} PREFIX=%{_prefix} NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
chmod +x %{buildroot}/%{_bindir}/%{name}

%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 13 2017 Petr Pisar <ppisar@redhat.com> - 0.9.1-8
- perl dependency renamed to perl-interpreter
  <https://fedoraproject.org/wiki/Changes/perl_Package_to_Install_Core_Modules>

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 21 2014 Ricky Elrod <codeblock@fedoraproject.org> - 0.9.1-3
- Add missing BR.

* Sun Mar 16 2014 Ricky Elrod <codeblock@fedoraproject.org> - 0.9.1-2
- Add a period to description.
- Move the build process to build section.
- Use mandir macro instead of hardcoded path.

* Sun Mar 16 2014 Ricky Elrod <codeblock@fedoraproject.org> - 0.9.1-1
- Initial build.
