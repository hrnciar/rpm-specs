%global __cmake_in_source_build 1

%global  checkout   be99c1cea6c5e2cf012fdaef8910176cde9ac2d3
%global  date       20150925

Name:    fido-pi
Summary: Protein identification in MS/MS proteomics
Version: 0
Release: 0.18.%{date}git%(echo %{checkout} | cut -c-6)%{?dist}
License: MIT
URL:     https://github.com/hendrikweisser/Fido
Source0: https://github.com/hendrikweisser/Fido/archive/%{checkout}.zip#/Fido-%{checkout}.zip

BuildRequires: cmake, gcc, gcc-c++

%description
Fido is a tool used in the area of computational proteomics.
It calculates posterior probabilities for protein
identifications based on database searches of tandem mass spectra.

%prep
%setup -q -n Fido-%{checkout}

%build
export CXXFLAGS="-std=c++14 $RPM_OPT_FLAGS"
mkdir -p build && pushd build
%cmake -DCMAKE_BUILD_TYPE:STRING=Release -DCMAKE_VERBOSE_MAKEFILE:BOOL=TRUE \
 -DCMAKE_SKIP_RPATH:BOOL=YES -DCMAKE_SKIP_INSTALL_RPATH:BOOL=YES -DCMAKE_BINARY_DIR:PATH=%{_bindir} ..
%make_build
popd

%install
## Manual installation
mkdir -p %{buildroot}%{_bindir}
install -pm 755 build/Fido %{buildroot}%{_bindir}
install -pm 755 build/FidoChooseParameters %{buildroot}%{_bindir}

%files
%license *license.txt
%doc *.md
%{_bindir}/Fido*

%changelog
* Tue Aug 18 2020 Jeff Law <law@redhat.com> - 0-0.18.20150925gitbe99c1
- Force C++14 as this code is not C++17 ready

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.17.20150925gitbe99c1
- Second attempt - Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild
- Enable cmake_in_source_build

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.16.20150925gitbe99c1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.15.20150925gitbe99c1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.14.20150925gitbe99c1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.13.20150925gitbe99c1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.12.20150925gitbe99c1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 22 2018 Antonio Trande <sagitter@fedoraproject.org> - 0-0.11.20150925gitbe99c1
- Add gcc gcc-c++ BR

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10.20150925gitbe99c1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 05 2018 Antonio Trande <sagitter@fedoraproject.org> 0-0.9.20150925gitbe99c1
- Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.20150925gitbe99c1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.20150925gitbe99c1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.20150925gitbe99c1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.20150925gitbe99c1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Oct 21 2015 Antonio Trande <sagitter@fedoraproject.org> 0-0.4.20150925gitbe99c1
- Rebuild

* Wed Oct 21 2015 Antonio Trande <sagitter@fedoraproject.org> 0-0.3.20150925gitbe99c1
- Commit #be99c1

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.2.20150209git281e4d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 27 2015 Antonio Trande <sagitter@fedoraproject.org> 0-0.1.20150209git281e4d
- First package
