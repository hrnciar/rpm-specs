Name:          crrcsim-addon-models
Version:       0.2.0
Release:       15%{?dist}
Summary:       Model-Airplane Flight Simulation Program addon models
License:       CC-BY
URL:           http://sourceforge.net/apps/mediawiki/crrcsim/
Source0:       http://prdownloads.sourceforge.net/crrcsim/%{name}/%{name}-%{version}.zip
Source1:       http://creativecommons.org/licenses/by/3.0/legalcode.txt
Source2:       crrcsim-addon-models-license-question-arthur.eml
Source3:       crrcsim-addon-models-license-question-jan.eml
Requires:      crrcsim >= 0.9.5
BuildArch:     noarch


%description
Addon models for Crrcsim


%prep
%setup -qcn %{name}-%{version}

# Correct EOL (preserve timestamps).
for i in \
    Readmefirst_Ellipse.txt \
    Readmefirst_Nyx.txt \
    Readmefirst_Europhia2k.txt \
    Readmefirst_Fireworks3.txt \
    Readmefirst_Skorpion.txt \
    Readmefirst_Freestyler.txt \
    Readmefirst_Crossfire.txt \
    install-cam.txt \
    Readmefirst_Erwin.txt; do
        sed 's#\r##g' documentation/$i > documentation/$i.tmp && \
        touch -r documentation/$i documentation/$i.tmp && \
        mv documentation/$i.tmp documentation/$i
done


%build


%install
mkdir -p %{buildroot}/%{_datadir}/crrcsim/

# Remove duplicates and older versions
rm documentation/Readmefirst_Crossfire.txt

rm models/Crossfire.xml \
   models/Erwin.xml \
   models/PilatusB4.xml \
   models/supra.xml

rm objects/Crossfire.ac \
   objects/Erwin.ac \
   objects/Fireworks_C.ac \
   objects/supra.ac

rm textures/CrossfireTexture.rgb \
   textures/Erwin.rgb \
   textures/Fireworks2.rgb \
   textures/PilB4Texture.rgb \
   textures/supra_texture_256.rgb

cp -ar models objects textures %{buildroot}/%{_datadir}/crrcsim
cp -p %{SOURCE1} %{SOURCE2} %{SOURCE3} .


%files
%doc documentation/*.txt legalcode.txt *.eml
%{_datadir}/crrcsim/models/*.xml
%{_datadir}/crrcsim/objects/*.ac
# Already exists in crrcsim-v0.9.13
%exclude %{_datadir}/crrcsim/objects/PilatusB4.ac
%{_datadir}/crrcsim/textures/*.rgb


%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Dec 21 2017 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0.2.0-9
- Exclude PilatusB4 object which exists in crrcsim-v0.9.13 (rhbz#1510107)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 28 2013 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0.2.0-2
- preserve timestamps during EOL conversion,
- license clarification e-mails added.

* Wed Jul 11 2012 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0.2.0-1
- initial RPM release.
