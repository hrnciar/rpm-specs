%global git_date   20180313
%global git_commit 16680f8688ffcd467d2eb2146a9ce0343404581d
%global git_commit_short %(c="%{git_commit}"; echo "${c:0:8}")

Version: 163840
Release: 3.%{git_date}git%{git_commit_short}%{?dist}

URL: https://www.hanyang.co.kr/hygothic/

%global foundry  HanYang
%global fontlicense  OFL
%global fontlicenses  OFL.txt

%global fontfamily  Gothic A1
%global fontsummary  HanYang Gothic A1, an elegant Korean and Latin font

%global fontdescription  %{expand:HanYang I&C Co's Gothic A1 is an elegant font for Korean and Latin text,
available in 9 weights.}

%global fonts  *.ttf
%global fontconfs  %{SOURCE10}


# Archive created by running the gothicA1-fetch.sh script (see Source99)
%global archivename HanYang-GothicA1-%{git_commit}
Source0: %{archivename}.zip

Source10: 60-%{fontpkgname}.xml

# A script to fetch the font files from Google Fonts repo on GitHub
Source99: gothicA1-fetch.sh


%fontpkg


%prep
%setup -q -n %{archivename}


%build
%fontbuild


%install
%fontinstall


%check
%fontcheck


%fontfiles


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 163840-3.20180313git16680f86
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 18 2020 Artur Iwicki <fedora@svgames.pl> - 163840-2.20180313git16680f86
- Add a basic fontconfig file

* Fri May 15 2020 Artur Iwicki <fedora@svgames.pl> - 163840-1.20180313git16680f86
- Initial packaging
