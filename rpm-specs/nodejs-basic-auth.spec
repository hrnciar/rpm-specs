%{?nodejs_find_provides_and_requires}

%global enable_tests 1
%global packagename basic-auth

Name:		nodejs-%{packagename}
Version:	1.1.0
Release:	8%{?dist}
Summary:	Generic basic auth Authorization header field parser for whatever
License:	MIT
URL:		https://github.com/jshttp/basic-auth
Source0:	https://github.com/jshttp/basic-auth/archive/v%{version}.tar.gz

ExclusiveArch:	%{nodejs_arches} noarch
BuildArch:	noarch

BuildRequires:	nodejs-packaging
Requires:	nodejs

%if 0%{?enable_tests}
BuildRequires:	npm(mocha)
# not packaged
#BuildRequires:  npm(eslint)
#BuildRequires:  npm(eslint-config-standard)
#BuildRequires:  npm(eslint-plugin-markdown)
#BuildRequires:  npm(eslint-plugin-promise)
#BuildRequires:  npm(eslint-plugin-standard)
%endif

%description
Generic basic auth Authorization header field parser for NodeJS

%prep
%setup -q -n %{packagename}-%{version}

%build
# nothing to do!

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr package.json *.js \
	%{buildroot}%{nodejs_sitelib}/%{packagename}

%nodejs_symlink_deps


%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
/usr/bin/mocha --check-leaks --reporter spec --bail
%endif

%files
%{!?_licensedir:%global license %doc}
%doc README.md HISTORY.md
%license LICENSE
%{nodejs_sitelib}/%{packagename}

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 11 2019 Jared K. Smith <jsmith@fedoraproject.org> - 1.1.0-7
- Remove unneeded calls to npm(istanbul)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Feb 14 2017 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.1.0-1
- Update

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat May 14 2016 Jared Smith <jsmith@fedoraproject.org> - 1.0.4-1
- Update to upstream 1.0.4 release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Oct 09 2015 Jared Smith <jsmith@fedoraproject.org> - 1.0.3-3
- Support building under EL6

* Wed Oct 07 2015 Jared Smith <jsmith@fedoraproject.org> - 1.0.3-2
- Add missing BuildRequires for mocha when enabling tests

* Wed Oct 07 2015 Jared Smith <jsmith@fedoraproject.org> - 1.0.3-1
- Initial packaging
