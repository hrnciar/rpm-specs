%global debug_package %{nil}

Name:		gimp-dbp
Version:        1.1.9
Release:        21%{?dist}
Summary:        Graphical batch processing for Gimp, no scripting knowledge required

License:        GPLv2+
URL:            http://www.ozemail.com.au/~hodsond/dbp.html
Source0:        http://www.ozemail.com.au/~hodsond/dbpSrc-1-1-9.tgz
Source1:	gimp-dbp.metainfo.xml

BuildRequires:	gcc-c++
BuildRequires:  gimp-devel
Requires:       gimp


%description
David's Batch Processor (DBP) is a simple batch processing plugin for the Gimp.
It allows the user to automatically perform operations, such as re-size, on a 
collection of image files. Its main advantage is that the user does not have to
learn a scripting language. Like the Gimp itself, DBP relies on a graphical
interface.


%prep
%autosetup -n dbp-%{version}


%build
# export CPPFLAGS="%{optflags}"
# make 
%make_build

%install
mkdir -p %{buildroot}%{_libdir}/gimp/2.0/plug-ins/
install -m 755 dbp %{buildroot}%{_libdir}/gimp/2.0/plug-ins/
# Add AppStream metadata
install -Dm 0644 -p %{SOURCE1} \
	%{buildroot}%{_datadir}/metainfo/%{name}.metainfo.xml

%files
%doc dbp.html
%{_libdir}/gimp/2.0/plug-ins/dbp
%{_datadir}/metainfo/%{name}.metainfo.xml

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.9-21
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.9-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.9-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.9-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.9-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.9-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 23 2018 Luya Tshimbalanga <luya@fedoraproject.org> - 1.1.9-15
- Update spec to new packaging guideline standard

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.9-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.9-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.9-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Mar 13 2016 Luya Tshimbalanga <luya@fedoraproject.org> - 1.1.9-9
- Added appstream metadata file (rhbz#1317193)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.1.9-6
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Mar 17 2013 Palle Ravn <ravnzon@gmail.com> 1.1.9-2
- Fix lib path
- Do not delete files in %%prep

* Thu Mar 7 2013 Palle Ravn <ravnzon@gmail.com> 1.1.9-1
- Initial package
