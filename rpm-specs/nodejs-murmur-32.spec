%{?nodejs_find_provides_and_requires}

%global packagename murmur-32
%global enable_tests 1

Name:		nodejs-murmur-32
Version:	0.1.0
Release:	6%{?dist}
Summary:	MurmurHash3 x86 32-bit implemented in JavaScript

License:	MIT
URL:		https://github.com/linusu/murmur-32
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz
Source1:	LICENSE-MIT.txt


ExclusiveArch:	%{nodejs_arches} noarch
BuildArch:	noarch

BuildRequires:	nodejs-packaging
BuildRequires:	npm(array-buffer-from-string)
BuildRequires:	npm(fmix)
BuildRequires:	npm(imul)

%if 0%{?enable_tests}
BuildRequires:	npm(arraybuffer-equal)
BuildRequires:	npm(hex-to-array-buffer)
%endif

%description
MurmurHash3 x86 32-bit implemented in JavaScript.


%prep
%autosetup -n package
cp -p %{SOURCE1} LICENSE

%build
# nothing to do!

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr package.json *.js \
	%{buildroot}%{nodejs_sitelib}/%{packagename}

%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
%if 0%{?enable_tests}
%{__nodejs} test.js
%else
%{_bindir}/echo -e "\e[101m -=#=- Tests disabled -=#=- \e[0m"
%endif

%files
%doc *.md
%license LICENSE
%{nodejs_sitelib}/%{packagename}

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Oct  3 2017 Jared Smith <jsmith@fedoraproject.org> - 0.1.0-1
- Initial packaging
