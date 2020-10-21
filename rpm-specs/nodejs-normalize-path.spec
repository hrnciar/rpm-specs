%global modname normalize-path

%if ! ( 0%{?fedora} || 0%{?rhel} >= 7 )
%{?nodejs_find_provides_and_requires}
%global nodejs_arches %{ix86} x86_64 %{arm}
%endif

Name:           nodejs-%{modname}
Version:        3.0.0
Release:        7%{?dist}
Summary:        Nodejs library for normalizing filesystem paths
License:        MIT
URL:            https://github.com/jonschlinkert/normalize-path
# Upstream does not want to include tests in the npm tarballs, 
# so we use a Github snapshot instead.
# https://github.com/jonschlinkert/normalize-path/issues/2#issuecomment-72331596
%global commit ea100bbecf851e2cc89e54e295e91af7b835fe63
Source0:        https://github.com/jonschlinkert/%{modname}/archive/%{commit}/%{modname}-%{version}.tar.gz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch
BuildRequires:  nodejs-packaging
BuildRequires:  mocha
BuildRequires:  npm(minimist)
BuildRequires:  npm(should)
BuildRequires:  /usr/bin/npm

%description
Normalize file path slashes to be unix-like forward slashes, regardless of OS 
(since in reality Windows doesn't care about slash direction anyway). Also 
condenses repeat slashes to a single slash and removes and trailing slashes.

%prep
%setup -q -n %{modname}-%{commit}

%build
# nothing to do

%check
%nodejs_symlink_deps --check
npm test

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{modname}
cp -pr package.json index.js \
    %{buildroot}%{nodejs_sitelib}/%{modname}/

%files
%doc README.md LICENSE
%{nodejs_sitelib}/%{modname}

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-7
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 30 2018 Dan Callaghan <dcallagh@redhat.com> - 3.0.0-1
- upstream release 3.0.0

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov 30 2015 Dan Callaghan <dcallagh@redhat.com> - 2.0.1-1
- upstream bug fix release 2.0.1: no longer strips leading ./

* Wed Nov 04 2015 Dan Callaghan <dcallagh@redhat.com> - 2.0.0-2
- added missing BR on minimist

* Wed Nov 04 2015 Dan Callaghan <dcallagh@redhat.com> - 2.0.0-1
- upstream release 2.0.0

* Tue Sep 01 2015 Dan Callaghan <dcallagh@redhat.com> - 1.0.0-1
- upstream release 1.0.0: paths are no longer forced to lower case

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Nov 12 2014 Dan Callaghan <dcallagh@redhat.com> - 0.3.0-1
- upstream release 0.3.0

* Sun Oct 12 2014 Dan Callaghan <dcallagh@redhat.com> - 0.1.1-1
- initial version
