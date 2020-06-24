%if 0%{?fedora} >= 31
%global forked_arcus 1
%else
%global forked_arcus 0
%endif

Name:           CuraEngine-lulzbot
Version:        3.6.21
Release:        4%{?dist}
Epoch:          1
Summary:        Engine for processing 3D models into G-code instructions for 3D printers
License:        AGPLv3+
URL:            https://code.alephobjects.com/diffusion/CTE/
# git clone https://code.alephobjects.com/diffusion/CTE/cura-engine.git
# cd cura-engine
# git checkout v3.6.21
## CANNOT USE git archive here, because we need to scrape the hash for version.json
# cd ..
# mv cura-engine CuraEngine-lulzbot-%%{version}
# tar cvfz CuraEngine-lulzbot-%%{version}.tar.gz CuraEngine-lulzbot-%%{version}
Source0:        CuraEngine-lulzbot-%{version}.tar.gz
# The cmake stuff would attempt to git clone this:
# TODO package on it's own
%global stb_commit e6afb9cbae4064da8c3e69af3ff5c4629579c1d2
Source1:        https://github.com/nothings/stb/archive/%{stb_commit}.tar.gz
Provides:       bundled(stb) = %stb_commit
BuildRequires:  gcc
BuildRequires:  gcc-c++
%if %{forked_arcus}
BuildRequires:  libarcus-lulzbot-devel >= %{version}
%else
BuildRequires:  libarcus-devel >= 3.6.0
%endif
BuildRequires:  polyclipping-devel >= 6.1.2
BuildRequires:  protobuf-devel
BuildRequires:  rapidjson-devel
BuildRequires:  cmake
BuildRequires:  git
%if %{forked_arcus}
Requires:       libarcus-lulzbot >= %{version}
%else
Requires:       libarcus >= 3.6.0
%endif

Patch0:         CuraEngine-lulzbot-3.2.17-no-rpath.patch
Patch1:         CuraEngine-lulzbot-3.2.17-no-static-libstdc++.patch
Patch2:         CuraEngine-lulzbot-3.6.3-optflags.patch

# https://github.com/Ultimaker/CuraEngine/issues/984
%if 0%{?fedora} >= 30
Patch4:         CuraEngine-lulzbot-gcc9.patch
%endif

%if %{forked_arcus}
# Need to use our arcus fork
Patch5:         CuraEngine-lulzbot-3.6.12-arcus-lulzbot.patch
%endif

%description
%{name} is a C++ console application for 3D printing G-code generation. It
has been made as a better and faster alternative to the old Skeinforge engine.

This is just a console application for G-code generation. For a full graphical
application look at cura-lulzbot which is the graphical frontend for %{name}.

%prep
%autosetup -p1 -n CuraEngine-lulzbot-%{version}
tar -xf %{SOURCE1}
mv stb-%{stb_commit} stb

GITHASH=`git rev-parse HEAD`

cat > version.json << EOF
{
  "engine": "$GITHASH"
}
EOF

# bundled libraries
rm -rf libs
sed -i 's|#include <clipper/clipper.hpp>|#include <polyclipping/clipper.hpp>|' src/utils/*.h src/*.cpp

# The -DCURA_ENGINE_VERSION does not work, so we sed-change the default value
sed -i 's/"DEV"/"%{version}"/' src/settings/Settings.h

%build
%{cmake} -DUSE_DISTRO_OPTIMIZATION_FLAGS:BOOL=ON -DUSE_SYSTEM_LIBS:BOOL=ON -DBUILD_SHARED_LIBS:BOOL=OFF -DStb_INCLUDE_DIRS:PATH=./stb -DCURA_ENGINE_VERSION:STRING=%{version} . # The lib is only intermediate
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}
mv %{buildroot}%{_bindir}/CuraEngine %{buildroot}%{_bindir}/CuraEngine-lulzbot
mkdir -p %{buildroot}%{_datadir}/%{name}/
cp -a version.json %{buildroot}%{_datadir}/%{name}/

%check
# Smoke test
%{buildroot}%{_bindir}/%{name} help

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/%{name}

%changelog
* Sun Jun 14 2020 Adrian Reber <adrian@lisas.de> - 1:3.6.21-4
- Rebuilt for protobuf 3.12

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.6.21-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 19 2019 Orion Poplawski <orion@nwra.com> - 1:3.6.21-2
- Rebuild for protobuf 3.11

* Mon Oct 21 2019 Tom Callaway <spot@fedoraproject.org> - 1:3.6.21-1
- update to 3.6.21

* Fri Aug 16 2019 Tom Callaway <spot@fedoraproject.org> - 1:3.6.18-1
- update to 3.6.18

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.6.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 12 2019 Tom Callaway <spot@fedoraproject.org> - 1:3.6.12-2
- use forked_arcus in rawhide

* Thu Jun 27 2019 Tom Callaway <spot@fedoraproject.org> - 1:3.6.12-1
- update to 3.6.12

* Thu May  2 2019 Tom Callaway <spot@fedoraproject.org> - 1:3.6.8-1
- update to 3.6.8

* Wed Apr 17 2019 Tom Callaway <spot@fedoraproject.org> - 1:3.6.6-1
- update to 3.6.6

* Wed Apr 17 2019 Tom Callaway <spot@fedoraproject.org> - 1:3.6.5-2
- fix libarcus requirements

* Wed Mar 27 2019 Tom Callaway <spot@fedoraproject.org> - 1:3.6.5-1
- update to 3.6.5

* Wed Feb 20 2019 Tom Callaway <spot@fedoraproject.org> - 1:3.6.3-1
- update to 3.6.3

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.2.32-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jan 19 2019 Tom Callaway <spot@fedoraproject.org> - 1:3.2.32-3
- rebuild for new libprotobuf

* Fri Nov 16 2018 Tom Callaway <spot@fedoraproject.org> - 1:3.2.32-1
- update to 3.2.32

* Mon Jul 30 2018 Tom Callaway <spot@fedoraproject.org> - 1:3.2.23-2
- do not copy the resources directory to itself (no-op)

* Mon Jul 30 2018 Tom Callaway <spot@fedoraproject.org> - 1:3.2.23-1
- update to 3.2.23

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.2.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 23 2018 Tom Callaway <spot@fedoraproject.org> - 1:3.2.21-1
- update to 3.2.21

* Wed May 23 2018 Tom Callaway <spot@fedoraproject.org> - 1:3.2.20-1
- update to 3.2.20

* Wed May  9 2018 Tom Callaway <spot@fedoraproject.org> - 1:3.2.19-1
- update to 3.2.19

* Mon Apr 23 2018 Tom Callaway <spot@fedoraproject.org> - 1:3.2.18-1
- update to 3.2.18

* Mon Apr 16 2018 Tom Callaway <spot@fedoraproject.org> - 1:3.2.17-1
- update to 3.2.17

* Wed Mar 14 2018 Tom Callaway <spot@fedoraproject.org> - 1:2.6.69-1
- update to 2.6.69

* Sat Feb 17 2018 Tom Callaway <spot@fedoraproject.org> - 1:2.6.66-3
- apply upstream valgrind fix to fix crash with gcc 8

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.6.66-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 17 2018 Tom Callaway <spot@fedoraproject.org> - 1:2.6.66-1
- update to 2.6.66

* Wed Jan  3 2018 Tom Callaway <spot@fedoraproject.org> - 1:2.6.63-1
- update to 2.6.63

* Fri Dec  8 2017 Tom Callaway <spot@fedoraproject.org> - 1:2.6.52-1
- update to 2.6.52

* Fri Oct 27 2017 Tom Callaway <spot@fedoraproject.org> - 1:2.6.43-1
- update to 2.6.43

* Fri Oct 27 2017 Tom Callaway <spot@fedoraproject.org> - 1:2.6.29-1
- update to 2.6.29

* Wed Aug 23 2017 Tom Callaway <spot@fedoraproject.org> - 1:2.6.23-1
- update to 2.6.23

* Mon Aug 14 2017 Tom Callaway <spot@fedoraproject.org> - 1:2.6.22-1
- update to 2.6.22

* Tue Aug  8 2017 Tom Callaway <spot@fedoraproject.org> - 1:2.6.21-1
- lulzbot fork

* Wed Jun 28 2017 Miro Hrončok <mhroncok@redhat.com> - 1:2.6.1-1
- Updated to 2.6.1

* Tue Jun 27 2017 Miro Hrončok <mhroncok@redhat.com> - 1:2.6.0-1
- Updated to 2.6.0

* Wed Jun 14 2017 Miro Hrončok <mhroncok@redhat.com> - 1:2.5.0-2
- Rebuilt for new protobuf 3.3.1

* Wed May 03 2017 Miro Hrončok <mhroncok@redhat.com> - 1:2.5.0-1
- Updated to 2.5.0

* Sun Dec 04 2016 Miro Hrončok <mhroncok@redhat.com> - 1:2.3.1-1
- New version scheme -> Introduce Epoch
- Updated
- SPEC rewritten

* Sun Sep 18 2016 Miro Hrončok <mhroncok@redhat.com> - 15.04-4
- Rebuilt for new polyclipping (#1159525)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 15.04-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jul 06 2015 Miro Hrončok <mhroncok@redhat.com> - 15.04-2
- Set the VERSION variable

* Sun Jul 05 2015 Miro Hrončok <mhroncok@redhat.com> - 15.04-1
- Update to 15.04

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14.12.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 14.12.1-2
- Rebuilt for GCC 5 C++11 ABI change

* Mon Dec 29 2014 Miro Hrončok <mhroncok@redhat.com> - 14.12.1-1
- Update to 14.12.1

* Thu Oct 23 2014 Miro Hrončok <mhroncok@redhat.com> - 14.03-3
- Rebuilt for new polyclipping

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14.03-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jun 23 2014 Miro Hrončok <mhroncok@redhat.com> - 14.03-1
- New version 14.03

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14.01-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Mar 09 2014 Miro Hrončok <mhroncok@redhat.com> - 14.01-1
- New version 14.01
- polyclipping 6.1.x
- Now with make test
- Rebuilt against new polyclipping release

* Sat Dec 14 2013 Miro Hrončok <mhroncok@redhat.com> - 13.11.2-1
- New version 13.11.2
- Makefile seding changed to reflect changes
- Clipper usage no longer need patching

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 13.06.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 22 2013 Miro Hrončok <mhroncok@redhat.com> - 13.06.3-3
- Rebuilt for new polyclipping

* Thu Jul 04 2013 Miro Hrončok <mhroncok@redhat.com> - 13.06.3-2
- Added some explaining comments

* Sun Jun 23 2013 Miro Hrončok <mhroncok@redhat.com> - 13.06.3-1
- New package
