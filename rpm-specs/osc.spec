# SUSE guys use OBS to automatically handle release numbers,
# when rebasing check what they are using on
# http://download.opensuse.org/repositories/openSUSE:/Tools/Fedora_31/src/
# update the obsrel to match the upstream release number
%global obsrel 303.1

# osc plugin support
%global osc_plugin_dir %{_prefix}/lib/osc-plugins

# for obs source services
%global obsroot %{_prefix}/lib/obs
%global obs_srcsvc_dir %{obsroot}/service

# Control building as Python 2 for <F30 / <EL8
%if (0%{?fedora} && 0%{?fedora} < 30) || (0%{?rhel} && 0%{?rhel} < 8)
%bcond_with python3
%else
%bcond_without python3
%endif

%if %{with python3}
%global __python %{__python3}
%else
%global __python %{__python2}
%endif

# Real release number
%global baserelease 1

Name:           osc
Summary:        Open Build Service Commander
Version:        0.169.1
# Bump the release as necessary to ensure we're one level up from upstream
Release:        %{obsrel}.%{baserelease}%{?dist}
License:        GPLv2+
URL:            https://github.com/openSUSE/osc
Source:         %{url}/archive/%{version}/%{name}-%{version}.tar.gz

# Proposed fixes
## Fix osc build --local-package runs
## From: https://github.com/openSUSE/osc/pull/573
Patch0101:      0101-Do-not-attempt-to-run-source-services-when-local-pac.patch
## Fix ElementTree imports to work with Python 3.9
## https://github.com/openSUSE/osc/pull/800
Patch0102:      0102-Fix-and-standardize-ElementTree-imports-for-Python-3.patch

BuildArch:      noarch

%if %{with python3}
BuildRequires:  python3-devel
BuildRequires:  python3-distro
BuildRequires:  python3-rpm
BuildRequires:  python3-progressbar2
Requires:       python3-distro
Requires:       python3-rpm
Requires:       python3-m2crypto
Requires:       python3-lxml
Requires:       python3-progressbar2
%else
BuildRequires:  python2-devel
BuildRequires:  python2-distro
BuildRequires:  python2-rpm
BuildRequires:  python2-progressbar2
Requires:       python2-distro
Requires:       python2-rpm
Requires:       m2crypto
Requires:       python2-lxml
Requires:       python2-progressbar2
%endif

%if 0%{?fedora} || 0%{?rhel} >= 8
Recommends:     obs-build
Recommends:     obs-service-source_validator
%else
Requires:       obs-service-source_validator
%endif

# To ensure functional parity
Conflicts:      obs-build < 20191205

%description
Commandline client for the Open Build Service.

See http://en.opensuse.org/openSUSE:OSC , as well as
http://en.opensuse.org/openSUSE:Build_Service_Tutorial for a general
introduction.


%prep
%autosetup -p1

#fixup encoding
iconv -f ISO8859-1 -t UTF-8 -o TODO.new TODO
mv TODO.new TODO

%build
%py_build

%install
%py_install

%__ln_s osc-wrapper.py %{buildroot}%{_bindir}/osc
%__mkdir_p %{buildroot}%{_localstatedir}/lib/osc-plugins
%__mkdir_p %{buildroot}%{_datadir}/bash-completion/completions/
install -Dm0644 dist/complete.csh %{buildroot}%{_sysconfdir}/profile.d/osc.csh
install -Dm0644 dist/complete.sh %{buildroot}%{_datadir}/bash-completion/completions/osc
install -Dm0755 dist/osc.complete %{buildroot}%{_datadir}/osc/complete

mkdir -p %{buildroot}%{obs_srcsvc_dir}

mkdir -p %{buildroot}%{osc_plugin_dir}

mkdir -p %{buildroot}%{_rpmconfigdir}/macros.d/

# osc rpm macros
cat > %{buildroot}%{_rpmconfigdir}/macros.d/macros.osc <<EOM
%%obs_srcsvc_dir %{obs_srcsvc_dir}
%%osc_plugin_dir %{osc_plugin_dir}
EOM


%files
%doc AUTHORS README TODO NEWS
%license COPYING
%{_bindir}/osc*
%{python_sitelib}/osc*
%{_sysconfdir}/profile.d/osc.csh
%{_datadir}/bash-completion/completions/osc
%dir %{_localstatedir}/lib/osc-plugins
%{_mandir}/man1/osc.*
%{_datadir}/osc
%{_rpmconfigdir}/macros.d/macros.osc
%dir %{obsroot}
%dir %{obs_srcsvc_dir}
%dir %{osc_plugin_dir}

%changelog
* Tue Jun 02 2020 Adam Williamson <awilliam@redhat.com> - 0.169.1-303.1.1
- Update to 0.169.1
- Drop merged or otherwise-fixed PRs
- Backport PR #800 to fix build with Python 3.9

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.167.1-281.1.5
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.167.1-281.1.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 31 2019 Neal Gompa <ngompa13@gmail.com> - 0.167.1-281.1.3
- Rebuild again to deal with random Koji+Bodhi breakage

* Fri Dec 27 2019 Neal Gompa <ngompa13@gmail.com> - 0.167.1-281.1.2
- Rebuild to deal with random Koji+Bodhi breakage

* Fri Dec 27 2019 Neal Gompa <ngompa13@gmail.com> - 0.167.1-281.1.1
- Update to 0.167.1
- Backport fix for regressions in osc chroot
- Refresh patch for fixing local builds
- Drop patch incorporated in this release
- Add patch to fix osc importsrcpkg on Python 3

* Mon Nov 18 2019 Neal Gompa <ngompa13@gmail.com> - 0.166.2-272.1.2
- Fix patch for replacing cgi.escape with html.escape

* Mon Nov 18 2019 Neal Gompa <ngompa13@gmail.com> - 0.166.2-272.1.1
- Update to 0.166.2
- Add fixes for Python 3.8 compatibility

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.165.1-255.1.2.3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.165.1-255.1.2.2
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.165.1-255.1.2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Neal Gompa <ngompa13@gmail.com> - 0.165.1-255.1.2
- Add patch proposed upstream to fix local builds

* Thu May 30 2019 Neal Gompa <ngompa13@gmail.com> - 0.165.1-255.1.1
- Update to 0.165.1
- Backport fixes from upstream for Python 3
- Drop patches incorporated in this release

* Sun Mar 24 2019 Neal Gompa <ngompa13@gmail.com> - 0.164.2-245.1.1
- Update to 0.164.2
- Add proposed patches to build for Python 3 for Fedora 30+
- Add Recommends for obs-build

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.163.0-237.1.1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Aug 23 2018 Neal Gompa <ngompa13@gmail.com> - 0.163.0-237.1.1
- Update to 0.163.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.162.1-230.1.1.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.162.1-230.1.1.2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.162.1-230.1.1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 15 2018 Neal Gompa <ngompa13@gmail.com> - 0.162.1-230.1.1
- Rebase to 0.162.1 to fix CVE-2017-9274

* Sun Nov 05 2017 Neal Gompa <ngompa13@gmail.com> - 0.161.1-224.1.1
- Rebase to 0.161.1

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.157.1-202.1.1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Mar 18 2017 Neal Gompa <ngompa13@gmail.com> - 0.157.1-202.1.1
- Rebase to 0.157.1

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.155.0-190.1.1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Aug 11 2016 Neal Gompa <ngompa13@gmail.com> - 0.155.0-190.1.1
- Rebase to 0.155.0

* Tue Jul 26 2016 Neal Gompa <ngompa13@gmail.com> - 0.154.0-187.1.1
- Rebase to 0.154.0
- Setup for working on EL7

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.151.1-166.2.1
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.151.1-165.2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.151.1-164.2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Feb 24 2015 Miroslav Suchý <msuchy@redhat.com> 0.151.1-163.2.1
- rebase to 0.140.1
- fixed shell command injection via crafted _service files CVE-2015-0778

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.140.1-109.1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.140.1-108.1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Miroslav Suchý <msuchy@redhat.com> 0.140.1-107.1.1
- add one number to release so we can distinguish from OpenSuse v-r
  (msuchy@redhat.com)
- rebase to 0.140.1 (msuchy@redhat.com)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.132.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.132.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.132.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jun 21 2011 Jerome Soyer <saispo@gmail.com> - 0.132.4-1
- Update to 0.132.4

* Thu Jun  9 2011 Jerome Soyer <saispo@gmail.com> - 0.132.1-2
- Fix non-arch dependent shell script in /usr/lib for multilib

* Wed Jun  8 2011 Jerome Soyer <saispo@gmail.com> - 0.132.1-1
- Update to 0.132.1
- Fix tab/space in SPEC file
- Add comment and command for tarball creation
- Fix libdir-macro-in-noarch-package

* Wed Jun  8 2011 Jerome Soyer <saispo@gmail.com> - 0.132.0-1
- Initial build
