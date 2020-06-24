%{?nodejs_find_provides_and_requires}

%global packagename nanomatch
%global enable_tests 1

Name:		nodejs-nanomatch
Version:	1.2.9
Release:	5%{?dist}
Summary:	Fast, minimal glob matcher for node.js

License:	MIT
URL:		https://github.com/micromatch/nanomatch.git
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz
# The test files are not included in the npm tarball.
# Source{1-9} are generated by running Source10, which pulls from the upstream
# version control repository.
Source1:	tests-%{version}.tar.bz2
Source2:	examples-%{version}.tar.bz2
Source10:	dl-tests.sh

# Support newer version of Snapdragon
Patch0:		nodejs-nanomatch_user-newer-snapdragon.patch

BuildArch:	noarch
ExclusiveArch: %{nodejs_arches} noarch

BuildRequires:	nodejs-packaging
BuildRequires:	npm(arr-diff)
BuildRequires:	npm(array-unique)
BuildRequires:	npm(is-odd)
BuildRequires:	npm(is-windows)
BuildRequires:	npm(fragment-cache)
BuildRequires:	npm(object.pick)
BuildRequires:	npm(snapdragon)
BuildRequires:	npm(snapdragon-capture)
BuildRequires:	npm(to-regex)

%if 0%{?enable_tests}
BuildRequires:	mocha
BuildRequires:	npm(bash-match)
BuildRequires:	npm(multimatch)
BuildRequires:	npm(for-own)
%endif

%description
Fast, minimal glob matcher for node.js. Similar to micromatch, minimatch and
multimatch, but complete Bash 4.3 wildcard support only (no support for
exglobs, posix brackets or braces).


%prep
%setup -q -n package
# setup the tests
%setup -q -T -D -a 1 -n package
# examples
%setup -q -T -D -a 2 -n package
# patch
%patch0 -p1

rm lib/.DS_Store

%nodejs_fixdep extend-shallow '~2.0.0'
%nodejs_fixdep kind-of '^3.2.2'
%nodejs_fixdep snapdragon '^0.12.0'

%build
# nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr package.json *.js lib/ \
	%{buildroot}%{nodejs_sitelib}/%{packagename}

%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
%if 0%{?enable_tests}
NODE_ENV=test %{_bindir}/mocha -R spec
%else
%{_bindir}/echo -e "\e[101m -=#=- Tests disabled -=#=- \e[0m"
%endif

%files
%doc *.md examples/
%license LICENSE
%{nodejs_sitelib}/%{packagename}

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Apr 18 2018 Jared K. Smith <jsmith@fedoraproject.org> - 1.2.9-1
- Initial packaging
