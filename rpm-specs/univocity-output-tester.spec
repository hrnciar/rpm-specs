Name:           univocity-output-tester
Summary:        Simple project to validate expected outputs of univocity parsers
Version:        2.1
Release:        2%{?dist}
License:        ASL 2.0

URL:            https://github.com/uniVocity/univocity-output-tester
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  maven-local

%description
This very simple project was created by univocity to help you validate
the expected results of test cases that produce data samples and
non-trivial outputs, such as XML, CSV, collections and arrays, etc.

It enforces a consistent and organized testing structure and enables
you to easily see what is going on with your tests if you want to.


%package        javadoc
Summary:        Javadoc for %{name}

%description    javadoc
API documentation for %{name}.


%prep
%autosetup

%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :nexus-staging-maven-plugin


%build
%mvn_build


%install
%mvn_install


%files -f .mfiles
%license LICENSE-2.0.html
%doc README.md

%files javadoc -f .mfiles-javadoc
%license LICENSE-2.0.html
%doc README.md


%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Oct 06 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1-1
- Initial packaging.

