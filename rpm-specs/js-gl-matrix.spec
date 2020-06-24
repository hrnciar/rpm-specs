

Name:          js-gl-matrix
Version:       2.4.0
Release:       6%{?dist}
Summary:       Javascript module designed to perform vector and matrix operations very fast
BuildArch:     noarch
License:       MIT
URL:           http://glmatrix.net/
Source0:       https://github.com/toji/gl-matrix/archive/v%{version}/gl-matrix-%{version}.tar.gz

BuildRequires: web-assets-devel

Requires:      web-assets-filesystem


%description
glMatrix is designed to perform vector and matrix operations stupidly fast!
By hand-tuning each function for maximum performance and encouraging
efficient usage patterns through API conventions, glMatrix will help you get
the most out of your browsers Javascript engine.

%prep
%setup -q -n gl-matrix-%{version}

%build

%install
%global installdir %{buildroot}%{_jsdir}/gl-matrix
mkdir -p %{installdir}/%{version}

cp -pr dist/* %{installdir}/%{version}

%files
%license LICENSE.md
%doc README.md VERSION
%{_jsdir}/gl-matrix


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Sep 24 2017 John Dulaney <jdulaney@fedoraproject.org> - 2.4.0-1
- New upstream release 2.4.0

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 27 2016 John Dulaney <jdulaney@fedoraproject.org> - 2.3.2-5
- Rebuild for F26

* Sun Jun 05 2016 John Dulaney <jdulaney@fedoraproject.org> - 2.3.2-4
- change install dir to gl-matrix

* Sat Jun 04 2016 John Dulaney <jdulaney@fedoraproject.org> - 2.3.2-3
- js-gl-matrix
- Add missing requires

* Fri May 27 2016 John Dulaney <jdulaney@fedoraproject.org> - 2.3.2-2
- cp -p -> cp -pr
- Better Summary
- Better Source0

* Wed May 25 2016 John Dulaney <jdulaney@fedoraproject.org> - 2.3.2-1
- Initial Packaging


