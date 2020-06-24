%global commit 9a348747642534bf40d63008ccd712b7bc35c636
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:		gimp-elsamuko
Version:	29
Release:	3%{?dist}
Summary:	Script collection for the GIMP
License:	GPLv3+
URL:		https://github.com/elsamuko/%{name}
Source0:	https://github.com/elsamuko/%{name}/archive/%{commit}/%{name}-%{commit}.tar.gz#/%{name}-%{shortcommit}.tar.gz
Requires:	gimp
BuildArch:	noarch

%description
Collection of scripts for the GIMP with various effects as; technicolor, 
round corners, Obama 'Hope', vintage look, sharpening, etc.

%prep
%autosetup -n %{name}-%{commit}

%build
## Nothing to build.

%install
install -d %{buildroot}%{_datadir}/gimp/2.10/scripts/
install -m 0644 -p scripts/*.scm -t %{buildroot}%{_datadir}/gimp/2.10/scripts/
%if 0%{?fedora} >= 21  
# Add AppStream metadata
install -Dm 0644 -p %{name}.metainfo.xml \
	%{buildroot}%{_metainfodir}/%{name}.metainfo.xml
%endif

%files
## Remember to add COPYING to docs, when it gets included upstream.
%doc README.md LICENSE
%{_datadir}/gimp/2.10/scripts/*.scm
%if 0%{?fedora} >= 21  
#AppStream metadata
%{_metainfodir}/%{name}.metainfo.xml
%endif

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 29-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 29-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 14 2019 Luya Tshimbalanga <luy@fedoraproject.org> - 29-1
- Upstream snapshot
- Modernize spec 
- Set new upstream url

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 26-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 26-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 26-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 26-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 26-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Luya Tshimbalanga <luya@fedoraproject.org> - 26-1
- Upstream update fixing metainfo.xml

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 24-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Feb 02 2015 Luya Tshimbalanga <luy@fedoraproject.org> - 24-6
- Lastest upstream update include metainfo.xml
- Dropped downstream metainfo.xml
- Made spec universal

* Sun Feb 01 2015 Luya Tshimbalanga <luy@fedoraproject.org> - 24-4
- Add metainfo files for software center

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 24-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Jan 03 2014 Palle Ravn <ravnzon@gmail.com> - 24-2
- Minor corrections

* Thu Dec 19 2013 Palle Ravn <ravnzon@gmail.com> - 24-1
- Initial package
