Name:           cloc
Version:        1.82
Release:        4%{?dist}
Summary:        Count lines of code
License:        GPLv2+
URL:            https://github.com/AlDanial/cloc
Source0:        https://github.com/AlDanial/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
%if 0%{?fedora}
BuildRequires:  perl-generators
%endif
BuildRequires:  perl-podlators
# Runtime
BuildRequires:  perl(Algorithm::Diff)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Glob)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(Parallel::ForkManager)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Regexp::Common)
BuildRequires:  perl(strict)
BuildRequires:  perl(Text::Tabs)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(warnings)
# Tests only
BuildRequires:  perl-interpreter
BuildRequires:  perl-Pod-Checker
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "$(perl -V:version)"; echo $version))

%{?perl_default_filter}

%description
A tool to count lines of code in various languages from a given directory.

%prep
%setup -q -n %{name}-%{version}/Unix

%build
# Nothing to do but run make anyway, in case anything ever changes
make %{_smp_mflags}

%install
make install DESTDIR="%{buildroot}"

#%check
#make test

%files
%license COPYING
%doc AUTHORS NEWS README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.82-4
- Perl 5.32 rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.82-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.82-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 18 2019 Rick Elrod <relrod@redhat.com> - 1.82-1
- Latest release.

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.72-8
- Perl 5.30 rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.72-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.72-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.72-5
- Perl 5.28 rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.72-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.72-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.72-2
- Perl 5.26 rebuild

* Thu May 11 2017 Ricky Elrod <relrod@redhat.com> - 1.72-1
- Disable tests for now, they depend on the cloc git repo for some reason.
- Latest release.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.70-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jul 04 2016 Ricky Elrod <relrod@redhat.com> - 1.70-1
- Latest release.

* Tue Jun 21 2016 Ricky Elrod <relrod@redhat.com> - 1.68-2
- Patch around perl.req bug.

* Tue Jun 21 2016 Ricky Elrod <relrod@redhat.com> - 1.68-1
- Latest release.

* Thu May 19 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.66-2
- Perl 5.24 re-rebuild of bootstrapped packages

* Wed May 18 2016 Ricky Elrod <relrod@redhat.com> - 1.66-1
- Bump to 1.66 with unbundled code (rhbz#1281479, rhbz#1324715, rhbz#1324791)

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.64-4
- Perl 5.24 rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.64-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 21 2016 Ricky Elrod <relrod@redhat.com> - 1.64-2
- Update bundled Regexp::Common for licensing issue (rhbz#1281479)
- (To do the above) Backport upstream commit 157c370.

* Thu Nov 12 2015 Petr Šabata <contyk@redhat.com> - 1.64-1
- 1.64 bump, rhbz#1236347
- Fix the deprecated code issue, sf bug#135, rhbz#1239400, rhbz#1271897
- Modernize and cleanup the spec file
- Package the docs and the license text
- Run the tests
- Fix the dep list
- Add perl MODULE_COMPAT
- Simplify the filters

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.62-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jul 30 2014 Ricky Elrod <relrod@redhat.com> - 1.62-1
- Update to upstream 1.62.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.60-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 17 2013 Ricky Elrod <codeblock@fedoraproject.org> - 1.60-1
- Update to upstream 1.60.
- Don't create a directory in %%setup.
- Fix rpmlint warning.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.58-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.58-6
- Perl 5.18 rebuild

* Mon Jul 1 2013 Ricky Elrod <codeblock@fedoraproject.org> - 1.58-5
- Rebuild on Rawhide for bz #927211.

* Tue May 14 2013 Ricky Elrod <codeblock@fedoraproject.org> - 1.58-4
- Enable the requires filter. (bz #962783)

* Mon May 13 2013 Ricky Elrod <codeblock@fedoraproject.org> - 1.58-3
- Refer to pod2man BR by path, the package name varies.

* Mon May 13 2013 Ricky Elrod <codeblock@fedoraproject.org> - 1.58-2
- Use the tarball release instead.
- Fix license field.

* Mon May 13 2013 Ricky Elrod <codeblock@fedoraproject.org> - 1.58-1
- Latest upstream release.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.56-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.56-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 14 2012 Ricky Elrod <codeblock@fedoraproject.org> - 1.56-5
- Remove the %%clean section altogether.

* Thu Jun 14 2012 Ricky Elrod <codeblock@fedoraproject.org> - 1.56-4
- Remove specfile actions that are no longer needed for post-EL5.

* Thu Jun 14 2012 Ricky Elrod <codeblock@fedoraproject.org> - 1.56-3
- Let rpmbuild compress the manpage automatically.

* Thu Jun 14 2012 Ricky Elrod <codeblock@fedoraproject.org> - 1.56-2
- Include documentation generated from a pod file.

* Fri May 25 2012 Ricky Elrod <codeblock@fedoraproject.org> - 1.56-1
- Initial build.
