%global image_major 4
%global image_minor 5
%global sources_minor 1
%global image_ver %{image_major}.%{image_minor}
%global image_rel 13680

%if 0%{?image_rel}
%global image_prel .%{?image_rel}
%global image_drel -%{?image_rel}
%endif

%global image_pfullver %{image_ver}%{?image_prel}
%global image_dfullver %{image_ver}%{?image_drel}

Name:           squeak-image
Version:        %{image_pfullver}
Release:        11%{?dist}
Summary:        The image files for Squeak

License:        MIT
URL:            http://www.squeak.org
Source0:        http://ftp.squeak.org/%{image_ver}/Squeak%{image_dfullver}.zip
Source1:        http://ftp.squeak.org/sources_files/SqueakV41.sources.gz
Source2:        squeak-image-doc.html

Requires:       squeak-vm >= 4.4.7.2357

BuildArch:      noarch

%description
This is the standard Squeak image as distributed by sqeak.org.
The Squeak image is split into three interdependent parts,
the .image file, the .changes file, and the .sources file.

%prep
%setup -q -c %{name}-%{version}
cp -p %SOURCE2 .

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_datadir}/squeak
# For squeak-image 4.3 (and maybe later) there is a subdir
[ -d Squeak%{image_dfullver} ] && cd Squeak%{image_dfullver}
cp Squeak%{image_dfullver}.image %{buildroot}%{_datadir}/squeak
cp Squeak%{image_dfullver}.changes %{buildroot}%{_datadir}/squeak
zcat %{SOURCE1} >%{buildroot}%{_datadir}/squeak/SqueakV%{image_major}%{sources_minor}.sources
cd %{buildroot}%{_datadir}/squeak
gzip Squeak%{image_dfullver}.image
gzip Squeak%{image_dfullver}.changes
gzip SqueakV%{image_major}%{sources_minor}.sources
ln -sf Squeak%{image_dfullver}.image.gz squeak.image.gz
ln -sf Squeak%{image_dfullver}.changes.gz squeak.changes.gz
ln -s SqueakV%{image_major}%{sources_minor}.sources.gz SqueakV%{image_major}.sources.gz
ln -s SqueakV%{image_major}%{sources_minor}.sources.gz squeak.sources.gz

%files
%doc squeak-image-doc.html
%{_datadir}/squeak/*

%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.13680-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.13680-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.13680-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.13680-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.13680-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.13680-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.13680-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.13680-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.5.13680-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.5.13680-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 20 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 4.5.13680-1
- New version
  Resolves: rhbz#1098695

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Nov 05 2012 Jaroslav Škarvada <jskarvad@redhat.com> - 4.3-1
- New version

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10.2.7179-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10.2.7179-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10.2.7179-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10.2.7179-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10.2.7179-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Nov 25 2008 Gavin Romig-Koch <gavin@redhat.com> - 3.10.2.7179-1
- Moved SqueakV39.sources into this rpm.
- Add a minimal doc page

* Sat Oct 22 2005 Gerard Milmeister <gemi@bluewin.ch> - 3.8.6665-1
- First Fedora release

