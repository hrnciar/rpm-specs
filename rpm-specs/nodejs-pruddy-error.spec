%{?nodejs_find_provides_and_requires}

%global packagename pruddy-error

# tests disabled to bootstrap newer npm(assume)
%global enable_tests 0

Name:		nodejs-pruddy-error
Version:	2.0.2
Release:	5%{?dist}
Summary:	Prettify given error object

License:	BSD
URL:		https://github.com/bigpipe/pruddy-error
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz

ExclusiveArch:	%{nodejs_arches} noarch
BuildArch:	noarch

BuildRequires:	nodejs-packaging
BuildRequires:	npm(left-pad)
BuildRequires:	npm(is-node)
%if 0%{?enable_tests}
BuildRequires:	npm(assume)
%endif

%description
Prettify given error object


%prep
%autosetup -n package

%build
# nothing to do!

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr *.json style-format.js failing-code.js failing-line.js \
	index.js format-text.js \
	%{buildroot}%{nodejs_sitelib}/%{packagename}

%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
%if 0%{?enable_tests}
%{__nodejs} --use_strict test.js
%else
%{_bindir}/echo -e "\e[101m -=#=- Tests disabled -=#=- \e[0m"
%endif

%files
%doc *.md
%license LICENSE
%{nodejs_sitelib}/%{packagename}

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 02 2018 Jared K. Smith <jsmith@fedoraproject.org> - 2.0.2-1
- Update to upstream 2.0.2 release

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Mar 29 2017 Jared Smith <jsmith@fedoraproject.org> - 1.0.2-1
- Initial packaging
