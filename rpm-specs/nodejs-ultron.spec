%global npm_name ultron
# Although there are tests
# the dependancies aren't in Fedora yet
%global enable_tests 0

%{?nodejs_find_provides_and_requires}

Summary:       Ultron is a high-intelligence robot
Name:          nodejs-%{npm_name}
Version:       1.1.1
Release:       6%{?dist}
License:       MIT
URL:           https://github.com/unshiftio/ultron
Source0:       http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
Source1:       https://raw.githubusercontent.com/unshiftio/ultron/%{version}/test.js
Source2:       https://raw.githubusercontent.com/unshiftio/ultron/%{version}/README.md

BuildRequires: nodejs-devel
%if 0%{?enable_tests}
BuildRequires:  npm(assume)
BuildRequires:  npm(eventemitter3)
BuildRequires:  npm(istanbul)
BuildRequires:  npm(mocha)
BuildRequires:  npm(pre-commit)
%endif
ExclusiveArch: %{nodejs_arches} noarch
BuildArch:     noarch

%description
Ultron is a high-intelligence robot. It gathers intelligence
so it can start improving upon his rudimentary design. It will
learn your event emitting patterns and find ways to exterminate
them. Allowing you to remove only the event emitters that you
assigned and not the ones that your users or developers assigned.
This can prevent race conditions, memory leaks and even file
descriptor leaks from ever happening as you won't remove clean
up processes.

%prep
%setup -q -n package
# Copy test.js
cp -ap %{SOURCE1} .
# Copy README.md
cp -ap %{SOURCE2} .

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pr index.js package.json test.js %{buildroot}%{nodejs_sitelib}/%{npm_name}


%if 0%{?enable_tests}
%check
mocha --reporter spec --ui bdd test.js
%endif

%files
%doc README.md
%license LICENSE
%{nodejs_sitelib}/%{npm_name}

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Dec 14 2017 Jared Smith <jsmith@fedoraproject.org> - 1.1.1-1
- Update to upstream 1.1.1 release

* Tue Sep 19 2017 Jared Smith <jsmith@fedoraproject.org> - 1.1.0-1
- Update to upstream 1.1.0 release

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Feb 16 2015 Troy Dawson <tdawson@redhat.com> - 1.0.1-3
- Added upsteam license file as source1

* Fri Feb 13 2015 Troy Dawson <tdawson@redhat.com> - 1.0.1-2
- Removed Group:
- Added a generic MIT license file as source1

* Tue Feb 03 2015 Troy Dawson <tdawson@redhat.com> - 1.0.1-1
- Initial spec file

