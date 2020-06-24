%global gitversion 9db45842

Name:           lv2-mdaEPiano
Version:        0
Release:        0.20.git%{gitversion}%{?dist}
Summary:        A port of the MDA EPiano VST plugin to LV2

License:        GPLv3+
URL:            https://github.com/rekado/%{name}
Source0:        %{name}-%{version}-git%{gitversion}.tar.bz2
# check out specific git revision sh lv2-mdaEPiano-snapshot.sh %%gitversion
Source1:        lv2-mdaEPiano-snapshot.sh

BuildRequires:  gcc-c++
BuildRequires:  lv2-devel
BuildRequires:  lv2-c++-tools-static
Requires:       lv2

%description
A port of the popular MDA EPiano VST plugin to LV2

%prep
%setup -q 
sed -i -e 's|-O $(WARNINGS)|$(CFLAGS)|'  src/Makefile

# Fix encoding issues
for file in LICENSE README.md; do
   sed 's|\r||' $file > $file.tmp
   iconv -f ISO-8859-1 -t UTF8 $file.tmp > $file.tmp2
   touch -r $file $file.tmp2
   mv -f $file.tmp2 $file
done

%build
cd src
make PREFIX=%{_prefix} CFLAGS="%optflags" %{?_smp_mflags}

%install
cd src
make install INSTALL_DIR=%{buildroot}%{_libdir}/lv2

%files
%doc README.md
%license LICENSE
%{_libdir}/lv2/lv2-mdaEPiano.lv2

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.20.git9db45842
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.19.git9db45842
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.18.git9db45842
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.17.git9db45842
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar 10 2018 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 0-0.16.git9db45842
- Added BR: gcc-c++
- Some cleanup
- Rebuild against lv2-c++-tools-1.0.5

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.15.git9db45842
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.14.git9db45842
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.13.git9db45842
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.12.git9db45842
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11.git9db45842
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.10.git9db45842
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0-0.9.git9db45842
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.8.git9db45842
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.7.git9db45842
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.6.git9db45842
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.5.git9db45842
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.4.git9db45842
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri May 11 2012 Brendan Jones <brendan.jones.it@gmail.com> 0-0.3.git9db45842
- Rebuild against new lv2 

* Tue Jan 24 2012 Brendan Jones <brendan.jones.it@gmail.com> 0-0.2.git9db45842
- Correct version, and update git script to remove .git
- Correct build flags, build requires lv2-c++-tools-static

* Sun Nov 27 2011 Brendan Jones <brendan.jones.it@gmail.com> 0-0.1.git5a4ab089
- Initial build

