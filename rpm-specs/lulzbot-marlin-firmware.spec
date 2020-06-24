%global gitrev 5f9c029d1
%global gitprorev aded3b617
%global gitbiorev 226bfbbb7
%global prover 2.0.0.144
%global biover 2.0.0.174
%global buildfromsource 1

Name:		lulzbot-marlin-firmware
Version:	1.1.9.34
Release:	10%{?dist}
Epoch:		1
Summary:	Marlin firmware files for the Lulzbot family of 3D printers
# this uses the arduino cross-compiler, so the output is arch-independent
BuildArch:	noarch
# Firmware source includes BSD, MIT, ISC, GPLv2+, GPLv3+, LGPLv2+, and LGPLv3+ licensed files
# Resulting combination is GPLv3+.
License:	GPLv3+
URL:		https://code.alephobjects.com/diffusion/MARLIN/
# https://www.lulzbot.com/learn/tutorials/firmware-flashing-through-cura
#
# If we pull from git:
# git clone https://code.alephobjects.com/diffusion/MARLIN/marlin.git
# cd marlin
# git checkout 5f9c029d1
# cd ..
# mv marlin/ lulzbot-marlin-firmware-1.1.9.34/
# tar cfz lulzbot-marlin-firmware-1.1.9.34.tar.gz lulzbot-marlin-firmware-1.1.9.34/
## PRO is using v2 code
# git clone https://code.alephobjects.com/diffusion/MARLIN/marlin.git
# cd marlin
# git checkout aded3b617
# cd ..
# mv marlin/ lulzbot-marlin-firmware-pro-2.0.0.144
# tar cfz lulzbot-marlin-firmware-pro-2.0.0.144.tar.gz lulzbot-marlin-firmware-pro-2.0.0.144/
## BIO is on a different checkout
# git clone https://code.alephobjects.com/diffusion/MARLIN/marlin.git
# cd marlin
# git checkout 226bfbbb7
# cd ..
# mv marlin/ lulzbot-marlin-firmware-bio-2.0.0.174
# tar cfz lulzbot-marlin-firmware-bio-2.0.0.174.tar.gz lulzbot-marlin-firmware-bio-2.0.0.174/

Source0:	lulzbot-marlin-firmware-%{version}.tar.gz
Source1:	lulzbot-marlin-firmware-pro-%{prover}.tar.gz
Source2:	lulzbot-marlin-firmware-bio-%{biover}.tar.gz
# Work around https://gcc.gnu.org/bugzilla/show_bug.cgi?id=71873
# Should not be needed when avr-gcc 7.0.0 arrives
Patch1:		lulzbot-marlin-firmware-1.1.5.64-set-fno-move-loop-invariants.patch
# Fix linking issue (-lgcc vs -gcc)
Patch2:		lulzbot-marlin-firmware-2.0.0.101-fix-lgcc.patch
BuildRequires:	arduino-core
BuildRequires:	git-core
BuildRequires:	arm-none-eabi-binutils-cs
BuildRequires:	arm-none-eabi-gcc-cs
BuildRequires:	arm-none-eabi-gcc-cs-c++
BuildRequires:	arm-none-eabi-newlib
Requires:	cura-lulzbot >= 3.6.8
# This is the best representation I could come up with for the bundled
# arduino bits and libraries
Provides:	bundled(arduino)
Provides:	bundled(arduino:LiquidCrystal)
Provides:	bundled(arduino:SPI)
Provides:	bundled(arduino:U8glib)

%description
%{summary}.

%package pro
Version:	%{prover}
Summary:	Marlin firmware files for the Lulzbot TAZ PRO family of 3D printers
Requires:	cura-lulzbot >= 3.6.8
# Just for common files
Requires:	lulzbot-marlin-firmware

%description pro
Marlin firmware files for the Lulzbot TAZ PRO family of 3D printers

%package bio
Version:        %{biover}
Summary:        Marlin firmware files for the Lulzbot TAZ BIO family of 3D printers
Requires:	cura-lulzbot >= 3.6.21
# Just for common files
Requires:	lulzbot-marlin-firmware

%description bio
Marlin firmware files for the Lulzbot TAZ BIO family of 3D printers

%global platform mega2560

%prep
%setup -q -a 1 -a 2
%patch1 -p1 -b .nmli
%patch2 -p1 -b .lgcc

%build
./build-lulzbot-firmware.sh 

# rename code in shell script assumes perl variant, we have util-linux variant
# this is more portable.
for f in build/*.hex; do mv "$f" "$(echo $f | cut -d '_' -f 1,3,5,6-)"; done

pushd lulzbot-marlin-firmware-pro-%{prover}
mkdir good-build
./build-lulzbot-firmware.sh Quiver_TAZPro AchemonSphinx_SmallLayer
cp build/* good-build/
./build-lulzbot-firmware.sh Quiver_TAZPro BandedTiger_HardenedSteel
cp build/* good-build/
./build-lulzbot-firmware.sh Quiver_TAZPro CecropiaSilk_SingleExtruderAeroV2
cp build/* good-build/
./build-lulzbot-firmware.sh Quiver_TAZPro DingyCutworm_HardenedSteelPlus
cp build/* good-build/
./build-lulzbot-firmware.sh Quiver_TAZPro Goldenrod_HardenedExtruder
cp build/* good-build/
./build-lulzbot-firmware.sh Quiver_TAZPro Quiver_DualExtruder
cp build/* good-build/
./build-lulzbot-firmware.sh Redgum_TAZWorkhorse AchemonSphinx_SmallLayer
cp build/* good-build/
./build-lulzbot-firmware.sh Redgum_TAZWorkhorse BandedTiger_HardenedSteel
cp build/* good-build/
./build-lulzbot-firmware.sh Redgum_TAZWorkhorse CecropiaSilk_SingleExtruderAeroV2
cp build/* good-build/
./build-lulzbot-firmware.sh Redgum_TAZWorkhorse DingyCutworm_HardenedSteelPlus
cp build/* good-build/
./build-lulzbot-firmware.sh Redgum_TAZWorkhorse Goldenrod_HardenedExtruder
cp build/* good-build/
./build-lulzbot-firmware.sh Redgum_TAZWorkhorse Yellowfin_DualExtruderV3
cp build/* good-build/

# rename code in shell script assumes perl variant, we have util-linux variant
# this is more portable.
# Workhorse
for f in good-build/*.hex; do mv "$f" "$(echo $f | cut -d '_' -f 1,3,5,6-)"; done

# Pro
for f in good-build/*.bin; do mv "$f" "$(echo $f | cut -d '_' -f 1,3,5,6-)"; done
popd

pushd lulzbot-marlin-firmware-bio-%{biover}
mkdir good-build
./build-lulzbot-firmware.sh KangarooPaw_Bio KangarooPaw_SingleExtruder
cp build/* good-build/

# Bio
for f in good-build/*.hex; do mv "$f" "$(echo $f | cut -d '_' -f 1,3,5,6-)"; done
popd

%install
mkdir -p %{buildroot}%{_datadir}/cura-lulzbot/firmware/
install -Dpm0644 build/*.hex %{buildroot}%{_datadir}/cura-lulzbot/firmware/

pushd lulzbot-marlin-firmware-pro-%{prover}
install -Dpm0644 good-build/*TAZPro*.bin %{buildroot}%{_datadir}/cura-lulzbot/firmware/
install -Dpm0644 good-build/*TAZWorkhorse*.hex %{buildroot}%{_datadir}/cura-lulzbot/firmware/
popd

pushd lulzbot-marlin-firmware-bio-%{biover}
install -Dpm0644 good-build/*Bio*.hex %{buildroot}%{_datadir}/cura-lulzbot/firmware/
popd

pushd %{buildroot}%{_datadir}/cura-lulzbot/
mkdir resources
ln -s ../firmware resources/firmware
popd

%files
%doc README.md
%license LICENSE
%{_datadir}/cura-lulzbot/firmware/*.hex
%exclude %{_datadir}/cura-lulzbot/firmware/*TAZWorkhorse*.hex
%{_datadir}/cura-lulzbot/resources/firmware

%files pro
%{_datadir}/cura-lulzbot/firmware/*.bin
%{_datadir}/cura-lulzbot/firmware/*TAZWorkhorse*.hex

%files bio
%{_datadir}/cura-lulzbot/firmware/*Bio*.hex

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.1.9.34-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Oct 21 2019 Tom Callaway <spot@fedoraproject.org> - 1:1.1.9.34-9
- add bio subpackage (Cura-LE 3.6.21)

* Fri Aug 16 2019 Tom Callaway <spot@fedoraproject.org> - 1:1.1.9.34-8
- update pro version for c-le 3.6.18

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.1.9.34-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 27 2019 Tom Callaway <spot@fedoraproject.org> - 1:1.1.9.34-6
- update pro version for c-le 3.6.12

* Thu May  2 2019 Tom Callaway <spot@fedoraproject.org> - 1:1.1.9.34-5
- update pro version for c-le 3.6.8

* Thu Apr 18 2019 Tom Callaway <spot@fedoraproject.org> - 1:1.1.9.34-4
- update pro version for c-le 3.6.6

* Thu Mar 28 2019 Tom Callaway <spot@fedoraproject.org> - 1:1.1.9.34-3
- preserve all PRO firmware files

* Wed Mar 27 2019 Tom Callaway <spot@fedoraproject.org> - 1:1.1.9.34-2
- add 2.0 PRO firmware subpackage

* Wed Feb 20 2019 Tom Callaway <spot@fedoraproject.org> - 1:1.1.9.34-1
- update to 1.1.9.34

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.1.9.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov 16 2018 Tom Callaway <spot@fedoraproject.org> - 1:1.1.9.28-1
- update to 1.1.9.28

* Mon Jul 30 2018 Tom Callaway <spot@fedoraproject.org> - 1:1.1.8.62-1
- update to 1.1.8.62

* Fri Jul 13 2018 Miro Hrončok <mhroncok@redhat.com> - 1:1.1.8.59-3
- Security fix for CVE-2018-1000537

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.1.8.59-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 23 2018 Tom Callaway <spot@fedoraproject.org> - 1:1.1.8.59-1
- update to 1.1.8.59

* Wed May 23 2018 Tom Callaway <spot@fedoraproject.org> - 1:1.1.8.51-1
- update to 1.1.8.51

* Tue May 22 2018 Tom Callaway <spot@fedoraproject.org> - 1:1.1.8.42-1
- update to 1.1.8.42

* Mon Apr 23 2018 Tom Callaway <spot@fedoraproject.org> - 1:1.1.8.29-1
- update to 1.1.8.29

* Wed Mar 14 2018 Tom Callaway <spot@fedoraproject.org> - 1:1.1.5.71-1
- update to 1.1.5.71

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.1.5.70-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 17 2018 Tom Callaway <spot@fedoraproject.org> 1:1.1.5.70-1
- update to 1.1.5.70

* Wed Jan  3 2018 Tom Callaway <spot@fedoraproject.org> 1:1.1.5.64-1
- bump epoch and use new firmware tree (whee!)

* Thu Nov 23 2017 Miro Hrončok <mhroncok@redhat.com> - 21.08-2
- Rebuilt to get it to f27

* Mon Aug 14 2017 Tom Callaway <spot@fedoraproject.org> - 21.08-1
- update to 21.08
- make symlink for cura2 compat
- do not build firmware from source (still no idea why it does not work)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 21.03-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 21.03-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan  4 2017 Tom Callaway <spot@fedoraproject.org> - 21.03-1
- update mini to 1.1.0.11

* Tue Nov 29 2016 Tom Callaway <spot@fedoraproject.org> - 21.00-2
- update mini to 1.1.0.10
- patch oliveoil* to build with gcc 6.2

* Fri Sep 30 2016 Tom Callaway <spot@fedoraproject.org> - 21.00-1
- update to 21.00 revisions
- drop patch merged upstream
- add TAZ6 moarstruder firmware

* Tue Sep  6 2016 Tom Callaway <spot@fedoraproject.org> - 20.03-2
- depend on cura-lulzbot
- do not own firmware dir (cura-lulzbot does)
- include README.md
- use smp_mflags
- add bundled provides
- add licensing comment
- update Gladiola to 1.1.0.9

* Wed Aug 31 2016 Tom Callaway <spot@fedoraproject.org> - 20.03-1
- update to firmware in cura-lulzbot 20.03

* Thu Jul 28 2016 Tom Callaway <spot@fedoraproject.org> - 20.01-1
- update to mini 1.1.0.5 f5e8154 (Gladiola)

* Tue Apr 12 2016 Tom Callaway <spot@fedoraproject.org> - 19.08-1
- initial package for lulzbot firmware (inspired a lot by Miro Hrončok's ultimaker2-marlin-firmware)
