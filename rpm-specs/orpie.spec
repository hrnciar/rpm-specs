Name:           orpie
Version:        1.5.2
Release:        14%{?dist}
Summary:        A full-screen console-based RPN calculator application
ExcludeArch:    armv7hl

License:        GPLv2 GPLv2+ LGPLv2
URL:            http://freecode.com/projects/orpie
Source0:        https://github.com/pelzlpj/orpie/releases/download/release-1.5.2/%{name}-%{version}.tar.gz
# GSL version 2 introduced minor incompatibilities with GSL version 1.6. The patch addresses those.
# This is tracked  by upstream here:
# https://github.com/pelzlpj/orpie/issues/1
Patch0:         patch-gsl-mgsl_sf.c.diff
# For some reason, compiling against Ocaml 4.04 cause the Ocaml compiler to complain
# about 'caml__frame' undeclared. Some searching yielded a simple solution. Upstream was made aware here:
# https://github.com/pelzlpj/orpie/issues/10
Patch1:         patch-mlgsl_error.c.diff
# This file declared two functions path0 removed. Added here:
# https://github.com/pelzlpj/orpie/issues/1
Patch2:         patch-gsl_sf.ml.diff
# Patch 3 is a hacky workaround for upstream not using ocamlfind to link against gsl dependency dynamically.
# See pull request here: https://github.com/pelzlpj/orpie/pull/2
# It also includes an explicit call ti use unsafe-string
# Upstream was notified here: https://github.com/pelzlpj/orpie/issues/14
# It further requires the linker option '-runtime-variant _pic' to work around the newer ocaml
# not being compiled with -Fpic
Patch3:         patch-Makefile.in.diff
# Because F26 adds -Werror=implicit-function-declaration
# Reported upstream here: https://github.com/pelzlpj/orpie/issues/11
Patch4:         patch-configure.diff
# Because F26 adds Werror=implicit-int
# Reported upstream here: https://github.com/pelzlpj/orpie/issues/11
Patch5:         patch-mlgsl_blas.h.diff

BuildRequires:  ocaml
BuildRequires:  gsl-devel
BuildRequires:  ncurses-devel
BuildRequires:  ocaml-camlp4-devel
BuildRequires:  ocaml-num-devel

%description
Orpie is a full-screen console-based RPN calculator that uses the curses
library.  Its operation is similar to that of modern HP calculators,
but data entry has been optimized for efficiency on a PC keyboard. Its
features include extensive scientific calculator functionality, command
completion, and a visible interactive stack.


%prep
%setup -q

%patch0 -p0
%patch1 -p0
%patch2 -p0
%patch3 -p0
%patch4 -p0
%patch5 -p0

%build
%configure
make


%install
make install DESTDIR=$RPM_BUILD_ROOT

%check || :
#make test
#make check


%files
%config(noreplace) %{_sysconfdir}/orpierc
%doc doc/manual.html doc/manual.pdf doc/manual.tex.in doc/TODO README ChangeLog
%license COPYING
%{_bindir}/*
%{_mandir}/man[^3]/*


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Aug 20 2019 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.5.2-13
- Rebuilt for GSL 2.6.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Aug 27 2018 Jared Wallace <jared@jared-wallace.com> - 1.5.2-11
- Patch for unsafe string
- Added '-runtime-variant _pic' linker flag
- Added ocaml-num-devel as a build require

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.5.2-9
- Escape macros in %%changelog

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Sun Jul 30 2017 Florian Weimer <fweimer@redhat.com> - 1.5.2-6
- Rebuild with binutils fix for ppc64le (#1475636)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 05 2016 Jared Wallace <jared-wallace@us.ibm.com> 1.5.2-4
- added two more patches because F26 made some changes to default compiler flags
* Tue Nov 29 2016 Jared Wallace <jared@jared-wallace.com> 1.5.2-3
- added three more patches to address issues exposed by Ocaml 4.04
* Fri Nov 11 2016 Jared Wallace <jared@jared-wallace.com> 1.5.2-2
- made release tag dynamic
- added additional licenses
- removed defattr line (unnecessary)
- removed hardened build flag (unnecessary)
- added multi-core compile flag
- changed COPYING from %%doc to %%license
* Wed Oct 05 2016 Jared Wallace <jared@jared-wallace.com> 1.5.2-1
- Cleaned up spec file
- Added patch to workaround GSL version 2 issue upstream
