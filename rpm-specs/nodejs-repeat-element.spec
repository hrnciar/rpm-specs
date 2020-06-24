%{?nodejs_find_provides_and_requires}

%global packagename repeat-element
%global enable_tests 1

Name:		nodejs-repeat-element
Version:	1.1.2
Release:	8%{?dist}
Summary:	Create an array by repeating the given value n times

License:	MIT
URL:		https://github.com/jonschlinkert/repeat-element.git
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz
# The test files are not included in the npm tarball.
# The 1.1.2 release is not tagged in github, so pull from master
Source1:	https://raw.githubusercontent.com/jonschlinkert/repeat-element/master/test.js
# The tests also need the 'benchmark' directory, which can be obtained by
# running the following command from a git checkout:
#
# git archive --prefix='benchmark/' --format=tar master:benchmark/ | bzip2 > benchmark-master.tar.bz2
Source2:	benchmark-master.tar.bz2


BuildArch:	noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:	nodejs-packaging
BuildRequires:	npm(chalk)
BuildRequires:	npm(glob)
BuildRequires:	npm(minimist)
%if 0%{?enable_tests}
BuildRequires:	mocha
%endif

%description
Create an array by repeating the given value n times.


%prep
%setup -q -n package
# setup the tests
cp -p %{SOURCE1} .
%setup -q -T -D -a 2 -n package



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
%{_bindir}/mocha
%else
%{_bindir}/echo "Tests disabled..."
%endif


%files
%{!?_licensedir:%global license %doc}
%doc *.md
%license LICENSE
%{nodejs_sitelib}/%{packagename}


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Feb  8 2016 Jared Smith <jsmith@fedoraproject.org> - 1.1.2-1
- Initial packaging
