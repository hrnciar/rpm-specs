Name:           java-packaging-howto
Version:        26.0.0
Release:        8%{?dist}
Summary:        Fedora Java packaging HowTo
License:        BSD
URL:            https://github.com/fedora-java/howto
BuildArch:      noarch

Source0:        https://github.com/fedora-java/howto/archive/%{version}.tar.gz

BuildRequires:  make
BuildRequires:  asciidoc
BuildRequires:  dia

Provides:       javapackages-tools-doc = %{version}-%{release}
Obsoletes:      javapackages-tools-doc < 4.7.0-7

%description
Offline version of Fedora Java packaging HowTo.

%prep
%setup -q -n howto-%{version}

%build
VERSION=%{version} make

%install
# nothing to install

%files
%license LICENSE
%doc index.html images

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 26.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 26.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 26.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 26.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 26.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 26.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 26.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Sep 01 2016 Michael Simacek <msimacek@redhat.com> - 26.0.0-1
- Review fixes

* Tue Aug 30 2016 Michael Simacek <msimacek@redhat.com> - 4.7.0-1
- Initial packaging after the split
