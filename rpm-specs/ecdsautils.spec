Name:           ecdsautils
Version:        0.3.2
Release:        12%{?dist}
Summary:        Tiny collection of programs used for ECDSA (keygen, sign, verify)

License:        BSD
URL:            https://github.com/tcatm/ecdsautils
Source0:        https://github.com/tcatm/ecdsautils/archive/v%{version}.tar.gz

# Create license text file
# Upstream pull request: https://github.com/tcatm/ecdsautils/pull/10
Patch1:         0001-Add-license-text-to-separate-file.patch

BuildRequires:  gcc
BuildRequires:  cmake
BuildRequires:  libuecc-devel

%description
This collection of ECDSA utilities can be used to sign and verify data in a
simple manner.


%prep
%setup -q
%patch1 -p1


%build
%cmake .
make %{?_smp_mflags}


%install
%make_install


%files
%doc README.md
%license COPYRIGHT
%{_bindir}/ecdsakeygen
%{_bindir}/ecdsasign
%{_bindir}/ecdsaverify


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Mar 01 2015 Felix Kaechele <heffer@fedoraproject.org> - 0.3.2-2
- add dedicated license file

* Tue Feb 10 2015 Felix Kaechele <heffer@fedoraproject.org> - 0.3.2-1
- initial package
