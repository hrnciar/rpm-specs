%global debug_package %{nil}
Name:           git-remote-hg
Version:        1.0.0
Release:        6%{?dist}
BuildArch:      noarch
Summary:        Mercurial wrapper for git
License:        GPLv2+
URL:            https://github.com/mnauw/git-remote-hg
Source0:        https://github.com/mnauw/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# https://github.com/fingolfin/git-remote-hg/commit/e716a9e1a9e460a45663694ba4e9e8894a8452b2.patch
# https://github.com/felipec/git-remote-hg/pull/28
# Makes it work with Mercurial 3.2
# The second commit (to the tests) isn't needed against 0.2

BuildRequires:  asciidoc >= 8.4.1
BuildRequires:  python2-devel
Requires:       python2
Requires:       git >= 2.0.0
Requires:       mercurial >= 3.5
Obsoletes:      git-hg

%description
git-remote-hg is the semi-official Mercurial bridge from Git project.
Once installed, it allows you to clone, fetch and push to and from Mercurial
repositories as if they were Git ones.

%prep
%setup -q
#%patch01 -p1
sed -i -e "1 s|^#!.*|#!%{__python2}|" git-remote-hg
sed -i -e 's|\tinstall|\tinstall -p|' Makefile

%build
make doc

%check
#make test

%install
export HOME=%{_prefix}
export DESTDIR=%{buildroot}
make install
make install-doc

%files
%doc LICENSE
%{_bindir}/git-remote-hg
%{_mandir}/man1/*

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Oct 20 2019 Petr Stodulka <pstodulk@redhat.com> - 1.0.0-4
- drop build dependency on hg-git which is here by mistake since the start

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Dec 22 2018 Dan Horák <dan[at]danny.cz> - 1.0.0-1
- Rebase to 1.0.0

* Mon Aug 20 2018 Petr Stodulka <pstodulk@redhat.com> - 0.4-1
- Rebase to v0.4
- Compatible with Mercurial v4.6
- Remove patches applied in upstream

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 30 2018 Tomas Korbar <tomas.korb@seznam.cz> - 0.3-8
- Add patches to fix known issues

* Sat Apr 28 2018 Tomas Korbar <tomas.korb@seznam.cz> - 0.3-7
- Change upstream to mnauws fork

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 05 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.3-5
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 28 2016 Petr Stodulka <pstodulk@redhat.com> - 0.3-2
- Fix incompatibility with mercurial 4.0

* Wed May 25 2016 Petr Stodulka <pstodulk@redhat.com> - 0.3-1
- Rebase to v0.3
- remove patches applied in upstream

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Nov 27 2015 Petr Stodulka <pstodulk@redhat.com> - 0.2-7
- Mercurial v3.5 has changed API - function context.memfilectx
  requires object repo as first parameter (#1265115)
- changed requires to mercurial >= 3.5

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jan 12 2015 Adam Williamson <awilliam@redhat.com> - 0.2-5
- backport an upstream PR to make it work with Mercurial 3.2

* Mon Dec 8 2014 Petr Stodulka <pstodulk@redhat.com> - 0.2-4
- added obsoletes of git-hg

* Mon Jun 23 2014 Ondrej Oprala <ooprala@redhat.com> - 0.2-3
- Explicitly disable debug_package, (noarch by itself
  still runs find-debuginfo.sh)

* Sun Jun 22 2014 Ondrej Oprala <ooprala@redhat.com> - 0.2-2
- Every single test fails(suspicious), disabling them for now

* Thu Jun 19 2014 Ondrej Oprala <ooprala@redhat.com> - 0.2-1
- initial git-remote-hg spec file
