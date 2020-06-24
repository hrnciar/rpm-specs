Name:           poly2tri
Version:        0.0
%global         rev 26242d0aa7b8
%global         date 20130501
%global         snapshot %{date}hg%{rev}
Release:        20.%{snapshot}%{?dist}
Summary:        A 2D constrained Delaunay triangulation library
License:        BSD
URL:            https://code.google.com/p/%{name}
# hg clone %%{url}
# rm -rf %%{name}/.hg
# tar -pczf %%{name}-%%{rev}.tar.gz %%{name}
Source0:        %{name}-%{rev}.tar.gz
# The Makefile was created for purposes of this package
# Upstream provides WAF, but it builds example apps and not the library
Source1:        %{name}-Makefile
BuildRequires:  gcc-c++
BuildRequires:  mesa-libGL-devel

%description
Library based on the paper "Sweep-line algorithm for constrained Delaunay
triangulation" by V. Domiter and and B. Zalik.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for %{name}.

%prep
%setup -qn %{name}
cp %{SOURCE1} %{name}/Makefile

iconv -f iso8859-1 -t utf-8 AUTHORS > AUTHORS.conv && \
touch -r AUTHORS AUTHORS.conv && \
mv AUTHORS.conv AUTHORS

%build
cd %{name}
CFLAGS="%{optflags}" LDFLAGS="%{build_ldflags}" make %{?_smp_mflags}
cd -

%install
install -Dpm0755 %{name}/lib%{name}.so.1.0 %{buildroot}%{_libdir}/lib%{name}.so.1.0
ln -s lib%{name}.so.1.0 %{buildroot}%{_libdir}/lib%{name}.so.1
ln -s lib%{name}.so.1.0 %{buildroot}%{_libdir}/lib%{name}.so

for H in %{name}/*/*.h %{name}/*.h; do
  install -Dpm0644 $H %{buildroot}%{_includedir}/$H
done

%files
%doc AUTHORS LICENSE README 
%{_libdir}/lib%{name}.so.*

%files devel
%doc AUTHORS LICENSE README 
%{_libdir}/lib%{name}.so
%{_includedir}/%{name}

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-20.20130501hg26242d0aa7b8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-19.20130501hg26242d0aa7b8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-18.20130501hg26242d0aa7b8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-17.20130501hg26242d0aa7b8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Feb 24 2018 Florian Weimer <fweimer@redhat.com> - 0.0-16.20130501hg26242d0aa7b8
- Use LDFLAGS from redhat-rpm-config

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-15.20130501hg26242d0aa7b8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-14.20130501hg26242d0aa7b8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-13.20130501hg26242d0aa7b8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-12.20130501hg26242d0aa7b8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-11.20130501hg26242d0aa7b8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0-10.20130501hg26242d0aa7b8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.0-9.20130501hg26242d0aa7b8
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0-8.20130501hg26242d0aa7b8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 29 2014 Miro Hrončok <mhroncok@redhat.com> - 0.0-7.20130501hg26242d0aa7b8
- Updated to latest revision

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0-6.20120407hgacf81f1f1764
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0-5.20120407hgacf81f1f1764
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Mar 20 2013 Miro Hrončok <mhroncok@redhat.com> - 0.0-4.20120407hgacf81f1f1764
- Using soname version 1.0
- Corrected Makefile to actually produce the library with soname version 1.0
- Added comment about the Makefile

* Wed Mar 13 2013 Miro Hrončok <mhroncok@redhat.com> - 0.0-3.20120407hgacf81f1f1764
- Using soname version 1.0.0 as upstream suggests so: http://code.google.com/p/poly2tri/issues/detail?id=66#c1

* Thu Mar 07 2013 Miro Hrončok <mhroncok@redhat.com> - 0.0-2.20120407hgacf81f1f1764
- Preserve AUTHORS timestamp
- Use %%{optflags}
- Add a comment about Makefile
- Added doc to -devel package

* Mon Feb 04 2013 Miro Hrončok <mhroncok@redhat.com> - 0.0-1.20120407hgacf81f1f1764
- Started
