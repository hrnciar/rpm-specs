Summary:	Firmware for Epson flatbed scanners
Name:		iscan-firmware
Version:	20190508
Release:	2%{?dist}
License:	Redistributable, no modification permitted
URL:		http://download.ebz.epson.net/dsc/search/01/search/
BuildArch:	noarch

# All firmware files can be downloaded individually, by searching per model, at:
# http://download.ebz.epson.net/dsc/search/01/search/

# The tarball contains a random version of the software, libraries and a firmware
# package (a "plugin"). The plugin package contains the firmware file.

# GT-F500, GT-F550, Perfection 2480 Photo, Perfection 2580 Photo
Source0:    iscan-plugin-gt-f500-1.0.0-1.c2.i386.rpm
# GT-9400UF, Perfection 3170 Photo
Source1:    iscan-plugin-gt-9400-1.0.0-1.c2.i386.rpm
# GT-F520, GT-F570, Perfection 3490 Photo, Perfection 3590 Photo
Source2:    iscan-plugin-gt-f520-1.0.0-1.c2.i386.rpm
# GT-F600, Perfection 4180 Photo
Source3:    iscan-plugin-gt-f600-1.0.0-1.c2.i386.rpm
# GT-X750, Perfection 4490 Photo
Source4:    iscan-plugin-gt-x750-2.1.2-1.x86_64.rpm
# GT-F650, GT-S600, Perfection V10, Perfection V100 Photo
Source5:    iscan-plugin-gt-s600-2.1.2-1.x86_64.rpm
# GT-F670, Perfection V200 Photo
Source6:    iscan-plugin-gt-f670-2.1.2-1.x86_64.rpm
# GT-F700, Perfection V350 Photo
Source7:    iscan-plugin-gt-f700-2.1.2-1.x86_64.rpm
# GT-1500, GT-D1000
Source8:    iscan-plugin-gt-1500-2.2.0-1.x86_64.rpm
# GT-F720, GT-S620, Perfection V30, Perfection V300 Photo
Source9:    esci-interpreter-gt-f720-0.1.1-2.x86_64.rpm
# GT-X770, Perfection V500 Photo
Source10:   iscan-plugin-gt-x770-2.1.2-1.i386.rpm
# GT-X820, Perfection V600 Photo
Source11:   iscan-plugin-gt-x820-2.2.0-1.x86_64.rpm
# GT-F730, GT-S630, Perfection V33, Perfection V330 Photo
Source12:   esci-interpreter-perfection-v330-0.2.0-1.x86_64.rpm
# GT-F740, GT-S640, Perfection V37, Perfection V370
Source13:   iscan-plugin-perfection-v370-1.0.0-2.x86_64.rpm
# Perfection V550 Photo
Source14:   iscan-plugin-perfection-v550-1.0.0-2.x86_64.rpm
# GT-S650, Perfection V19, Perfection V39
Source15:   imagescan-plugin-gt-s650-1.0.1-1epson4fedora30.x86_64.rpm
# GT-X830
Source16:   iscan-plugin-gt-x830-1.0.0-5.x86_64.rpm

%if 0%{?rhel} == 6
Requires:	udev
%else
Requires:	linux-firmware
%endif

%description
Firmware for the following Epson flatbed scanners:

* esfw32: Perfection 3170 PHOTO / GT-9400
* esfw41: Perfection 2480/2580 PHOTO / GT-F500/F550
* esfw43: Perfection 4180 PHOTO / GT-F600
* esfw52: Perfection 3490/3590 PHOTO / GT-F520/F570
* esfw54: Perfection 4490 PHOTO / GT-X750
* esfw66: Perfection V10/V100 PHOTO / GT-S600 / GT-F650
* esfw68: Perfection V350 PHOTO / GT-F700
* esfw7A: Perfection V200 PHOTO / GT-F670
* esfw7C: Perfection V500 PHOTO / GT-X770
* esfw86: GT-1500 / GT-D1000
* esfw8b: Perfection V30/V300 / GT-F720 / GT-S620
* esfwA1: Perfection V600 PHOTO / GT-X820
* esfwad: Perfection V33/V330 PHOTO / GT-F730 / GT-S630
* esfwdd: Perfection V37/V370 / GT-F740 / GT-S640
* esfweb: Perfection V550 PHOTO
* esfw010c: Perfection V19/V39 / GT-S650
* Esfw0111: GT-X830

%prep
%setup -c -T
for f in \
    %{SOURCE0} %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5} \
    %{SOURCE6} %{SOURCE7} %{SOURCE8} %{SOURCE9} %{SOURCE10} %{SOURCE11} \
    %{SOURCE12} %{SOURCE13} %{SOURCE14} %{SOURCE15} %{SOURCE16}; do
    rpm2cpio $f | cpio -idvm --no-absolute-filenames
done

find ./%{_docdir} -name "*txt" -exec mv {} . \;

for file in *.txt ; do
    iconv -f euc-jp -t UTF-8 -o $file.new $file && \
    touch -r $file $file.new && \
    mv $file.new $file
done

%build
# Nothing to build

%install
mkdir -p %{buildroot}/lib/firmware/epson
install -pm644 .%{_datadir}/{iscan,esci,utsushi}/*.bin %{buildroot}/lib/firmware/epson

%files
%{!?_licensedir:%global license %%doc}
%license AVASYSPL.en.txt EAPL.en.txt LICENSE.EPSON.en.txt
%lang(ja) %license AVASYSPL.ja.txt EAPL.ja.txt LICENSE.EPSON.ja.txt
/lib/firmware/epson

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20190508-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 19 2019 Simone Caronni <negativo17@gmail.com> - 20190508-1
- Check all firmwares, add GT-S650/GT-X830 firmwares dated 2019-05-08.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20130319-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20130319-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20130319-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20130319-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20130319-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20130319-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20130319-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20130319-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 01 2015 Simone Caronni <negativo17@gmail.com> - 20130319-1
- Add Perfection V550 firmware (#1212545).
- Add license macro.

* Tue Jan 13 2015 Simone Caronni <negativo17@gmail.com> - 20121031-3
- Add firmware name to description (eases configuration).
- Adjust source urls.
- Require linux-firmware on RHEL 7+ and Fedora.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20121031-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Nov 18 2013 Dominik Mierzejewski <rpm@greysector.net> 20121031-1
- point all URLs to new upstream
- mention all supported models in comments, too
- point some source URLs to smaller upstream rpms
- add firmware (2012-10-31) for GT-F740, GT-S640, Perfection V37/V370
- switch to versioning by date (of the latest firmware)
- drop some obsolete spec file constructs
- fix bogus date in changelog

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.26.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.26.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.26.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.26.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 26 2011 Dominik Mierzejewski <rpm@greysector.net> 2.26.4-1
- updated firmware source packages for GT-1500, V30/V300 (GT-F720), V33/V330,
  V200 PHOTO (GT-F670), V350 PHOTO (GT-F700), V10 / V100 PHOTO (GT-S600),
  4490 PHOTO (GT-X750), V500 PHOTP (GT-X770)

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.25.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Nov 21 2010 Dominik Mierzejewski <rpm@greysector.net> 2.25.1-1
- added firmwares for: V33/V330 PHOTO, V600 PHOTO

* Tue Aug 25 2009 Dominik Mierzejewski <rpm@greysector.net> 2.1.1-1
- updated firmwares for: 4490, GT-1500, V10/V100, V200, V30/V300, V350, V500

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Mar 03 2009 Dominik Mierzejewski <rpm@greysector.net> 2.1.0-3
- set version to that of the latest firmware package
- updated source url for Perfection V200 firmware
- added disttag

* Sun Mar 01 2009 Dominik Mierzejewski <rpm@greysector.net> 2.1.0-2
- changed licence tag
- added requires udev for /lib/firmware dir ownership
- added missing licence texts

* Tue Feb 03 2009 Dominik Mierzejewski <rpm@greysector.net> 2.1.0-1
- initial build
