%global forgeurl https://github.com/CyberShadow/znc-clientbuffer
%global commit 9766a4ad5d27e815bbbc8b6842e13b7b4b5826f6
%forgemeta

%global modname clientbuffer
%global znc_version %((znc -v 2>/dev/null || echo 'a 0') | head -1 | awk '{print $2}')

Name:           znc-%{modname}
Version:        0
Release:        0.17%{?dist}
Summary:        ZNC module for client specific buffers

License:        ASL 2.0
URL:            %forgeurl
Source0:        %forgesource

BuildRequires:  gcc-c++
BuildRequires:  zlib-devel
BuildRequires:  znc-devel
Requires:       znc%{?_isa} = %znc_version

%description
The client buffer module maintains client specific buffers for identified
clients.

%prep
%autosetup -n %{name}-%{commit}

%build
CXXFLAGS="%{optflags}" LDFLAGS="%{__global_ldflags}" znc-buildmod %{modname}.cpp

%install
install -Dpm0755 %{modname}.so %{buildroot}%{_libdir}/znc/%{modname}.so

%files
%{_libdir}/znc/%{modname}.so

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 22 2020 Jason L Tibbitts III <tibbs@math.uh.edu> - 0-0.15
- Rebuild for new znc.

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 29 2019 Jason L Tibbitts III <tibbs@math.uh.edu> - 0-0.13.git9766a4a
- Rebuild for new znc.

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.12.git9766a4a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 29 2019 Jason L Tibbitts III <tibbs@math.uh.edu> - 0-0.11.20190129git9766a4a
- Convert to forge macros.

* Wed Jan 23 2019 Pete Walter <pwalter@fedoraproject.org> - 0-0.10gitfe0f368
- Rebuild for ICU 63

* Tue Jul 31 2018 Jason L Tibbitts III <tibbs@math.uh.edu> - 0-0.9gitfe0f368
- Require specific version of znc, to avoid unexpected breakage when znc
  updates.  (Broken deps are better than a broken server.)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8gitfe0f368
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018 Pete Walter <pwalter@fedoraproject.org> - 0-0.7gitfe0f368
- Rebuild for ICU 62

* Fri Jun 01 2018 Jason L Tibbitts III <tibbs@math.uh.edu> - 0-0.6gitfe0f368
- Rebuild for new znc.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5gitfe0f368
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4gitfe0f368
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3gitfe0f368
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2gitfe0f368
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Aug 17 2016 Igor Gnatenko <ignatenko@redhat.com> - 0-0.1gitfe0f368
- Initial package
