%{?nodejs_find_provides_and_requires}

%global packagename arr-flatten
%global enable_tests 1

Name:		nodejs-arr-flatten
Version:	1.1.0
Release:	6%{?dist}
Summary:	Recursively flatten an array or arrays

License:	MIT
URL:		https://github.com/jonschlinkert/arr-flatten.git
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz
# The test files are not included in the npm tarball, and the 1.0.1 release has
# not yet been tagged in github, so pull from master for now
Source1:	https://raw.githubusercontent.com/jonschlinkert/arr-flatten/%{version}/test.js


BuildArch:	noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:	nodejs-packaging
%if 0%{?enable_tests}
BuildRequires:	mocha
BuildRequires:	npm(array-flatten)
%endif

%description
Recursively flatten an array or arrays. This is the fastest implementation of
array flatten.


%prep
%setup -q -n package
# setup the tests
cp -p %{SOURCE1} .

# remove unneeded executable bits
chmod -x ./*

%build
# nothing to do!

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr package.json index.js \
	%{buildroot}%{nodejs_sitelib}/%{packagename}

%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
%if 0%{?enable_tests}
%{_bindir}/mocha -R spec
%else
%{_bindir}/echo "Tests disabled..."
%endif


%files
%{!?_licensedir:%global license %doc}
%doc *.md
%license LICENSE
%{nodejs_sitelib}/%{packagename}


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 15 2017 Jared Smith <jsmith@fedoraproject.org> - 1.1.0-1
- Update to upstream 1.1.0 release

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb  3 2016 Jared Smith <jsmith@fedoraproject.org> - 1.0.1-1
- Initial packaging
