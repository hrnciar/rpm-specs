%global commit      788874a62eb7b7ed78ab3d7218a5cdd9fe346fb5
%global date        20200401
%global forgeurl    https://github.com/steinbergmedia/bravura

Version:        1.360
URL:            https://www.smufl.org/fonts/

%forgemeta

Release:        2%{?dist}

%global foundry          steinberg
%global fontlicense      OFL
%global fontlicenses     LICENSE.txt
%global fontdocs         README.md redist/bravura-text.md redist/FONTLOG.txt
%global fontdocsex       %{fontlicenses}

%global common_description %{expand:
Bravura is an OpenType music font developed for Steinberg's Dorico music
notation and composition software.  It is also the reference font for
Standard Music Font Layout (SMuFL), which provides a standard way of
mapping the thousands of musical symbols required by conventional music
notation into the Private Use Area in Unicode's Basic Multilingual Plane
for a single (format-independent) font.}

%global fontfamily0      Bravura
%global fontsummary0     Bravura music font
%global fonts0           redist/otf/Bravura.otf
%global fontconfs0       %{SOURCE1}
%global fontappstreams0  %{SOURCE2}
%global fontdescription0 %{expand:%{common_description}

This package contains the Bravura font family.  It is a Unicode typeface
designed by Steinberg for its music notation and scoring application.
}

# This can be removed when F36 reaches EOL
%global fontpkgheader0 %{expand:
Obsoletes:      steinberg-bravura-fonts-common < 1.360
Provides:       steinberg-bravura-fonts-common = %{version}-%{release}
}

%global fontfamily1      BravuraText
%global fontsummary1     Bravura text font
%global fonts1           redist/otf/BravuraText.otf
%global fontconfs1       %{SOURCE3}
%global fontappstreams1  %{SOURCE4}
%global fontdescription1 %{expand:%{common_description}

This package contains the Bravura Text font family.  It is a Unicode
typeface designed by Steinberg for its music notation and scoring
application.
}

# This can be removed when F36 reaches EOL
%global fontpkgheader1 %{expand:
Obsoletes:      steinberg-bravura-text-fonts < 1.360
Provides:       steinberg-bravura-text-fonts = %{version}-%{release}
}

Source0:        %{forgesource}
Source1:        %{foundry}-bravura.metainfo.xml
Source2:        65-%{fontpkgname0}.conf
Source3:        %{foundry}-bravura-text.metainfo.xml
Source4:        65-%{fontpkgname1}.conf

%fontpkg -a
%fontmetapkg

%prep
%forgesetup
 
%build
%fontbuild -a

%install
cd redist
# Install the SMuFL metadata
install -m 0755 -d %{buildroot}%{_datadir}/SMuFL/Fonts/bravura
install -m 0644 -p bravura_metadata.json \
  %{buildroot}%{_datadir}/SMuFL/Fonts/bravura
install -m 0755 -d %{buildroot}%{_fontdir}
ln -s %{_datadir}/SMuFL/Fonts/bravura/bravura_metadata.json \
      %{buildroot}%{_fontdir}/metadata.json
cd -

%fontinstall -a

%check
%fontcheck -a

%fontfiles -z 0
%{_datadir}/SMuFL/Fonts/bravura/bravura_metadata.json
%{_fontdir}/metadata.json

%fontfiles -z 1

%changelog
* Tue Apr  7 2020 Jerry James <loganjerry@gmail.com> - 1.360-2.20200401git788874a
- Fix Obsoletes (bz 1821488)

* Fri Apr  3 2020 Jerry James <loganjerry@gmail.com> - 1.360-1.20200401git788874a
- Version 1.360
- Comply with the new font guidelines

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.320-2.20191209.6aa3a10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 14 2019 Jerry James <loganjerry@gmail.com> - 1.320-1.20191209.6aa3a10
- Version 1.320

* Thu Sep 19 2019 Jerry James <loganjerry@gmail.com> - 1.277-1.20190423.ccc90dd
- Initial RPM
