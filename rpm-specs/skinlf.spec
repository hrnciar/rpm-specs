%define cvsver cvs20091205

Name:		skinlf	
Version:	6.7
Release:	27.%{cvsver}%{?dist}
Summary:	Skin look and feel Skinning library for java

License:	ASL 2.0
URL:		http://skinlf.dev.java.net/	

Source0:	%{name}-%{version}%{cvsver}-clean.tar.gz
# Original Source# Contains code that we cannot ship. 
# Download the upstream tarball and invoke this script while in the
# tarball's directory. Must perform co as specified in sh file.
# ./skinlf-generate-cvs-tarball.sh
Source1:	%{name}-generate-cvs-tarball.sh


BuildArch:	noarch

#See http://bollin.googlecode.com/svn/libskinlf-java/trunk
#for patchset maintained by Scilab developer, Sylvestre Ledru.
# These patches have been modified.
Patch0:		skinlf-nosun-jimi-patch.patch	
#org.apache.xpath has been removed from JDK1.5 and above
#patch to use com.sun.org.apache.xpath.internal.XPathAPI instead 
Patch1:		skinlf-sun-jdk1.5-xpath-patch.patch

BuildRequires:	ant
BuildRequires:	laf-plugin
BuildRequires:	dos2unix
BuildRequires:	java-devel >= 1:1.6.0
BuildRequires:	jpackage-utils
BuildRequires:	ant

Requires:	java >= 1:1.6.0
Requires:	jpackage-utils

#This depends upon laf-plugin
#https://bugzilla.redhat.com/show_bug.cgi?id=461407
Requires:	laf-plugin




%description
Skin Look And Feel is a java framework that is able to read GTK (The
Gimp ToolKit) and KDE (The K Desktop Environment) skins to enhance
your application.
SkinLF supports GUI controls such as Buttons, Checks, Radios, Scrollbars,
Progress Bar, Lists, Tables, Internal Frames, Colors, Background
Textures, Regular Windows.

%prep
%setup -q -n %{name} 
%patch0
%patch1

#convert Doc files to unix format
for file in AUTHORS README LICENSE LICENSE_nanoxml ;
do
	sed 's/\r//' $file > $file.new && \
	touch -r $file $file.new && \
	mv $file.new $file
done

#Remove jar files
rm -f ./lib/examples.jar 
rm -f ./lib/nativeskin.jar 
rm -f ./lib/skinlf.jar 
rm -f ./lib/sunawt.jar
rm -f ./lib/laf-plugin*.jar
rm -f ./lib/proguard.jar
rm -f ./lib/imageconversion.jar

#Sanitise package -- disallow jar files
JAR_files=""
for j in $(find -name \*.jar); do
if [ ! -L $j ] ; then
	JAR_files="$JAR_files $j"
	fi
done

if [ ! -z "$JAR_files" ] ; then
	echo "These JAR files should be deleted and symlinked to system JAR files: $JAR_files"
	#Uncomment this line before accepting package
	exit 1
fi


%build
export CLASSPATH=$(build-classpath laf-plugin)
ant -Dbuild.sysclasspath=first
#Construct-a-jar Dont use ant jar as it tries to unpack laf-plugin
pushd build/classes
jar cf %{name}.jar .
popd


%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/%{_javadir}
install -m644 ./build/classes/%{name}.jar -D %{buildroot}%{_javadir}/%{name}.jar 
cd %{buildroot}%{_javadir}/

%files
%doc README LICENSE LICENSE_nanoxml
%{_javadir}/%{name}.jar

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.7-27.cvs20091205
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.7-26.cvs20091205
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.7-25.cvs20091205
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.7-24.cvs20091205
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.7-23.cvs20091205
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.7-22.cvs20091205
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.7-21.cvs20091205
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 6.7-20.cvs20091205
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.7-19.cvs20091205
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.7-18.cvs20091205
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Dec 01 2013 <mycae(a!t)gmx.com> - 6.7-17.cvs20091205
- Fix bug 1022164

* Fri Aug 09 2013 <mycae(a!t)gmx.com> - 6.7-16.cvs20091205
- Fix FTBFS due to ant-nodeps renamed to ant (https://lists.fedoraproject.org/pipermail/java-devel/2013-April/004777.html)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.7-15.cvs20091205
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.7-14.cvs20091205
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.7-13.cvs20091205
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.7-12.cvs20091205
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.7-11.cvs20091205
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

*Sat Dec 05 2009 <mycae(a!t)yahoo.com> 6.7-10.cvs20091205
- Additional ASL Files

*Sat Sep 26 2009 <mycae(a!t)yahoo.com> 6.7-9.cvs20090501
- Modify to ASL 2.0, upstream has relicenced - fix bug #524784
- Use CVS co, as upstream does not provide release

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

*Sat Dec 06 2008 <mycae(a!t)yahoo.com> 6.7-6
- Fixed jar dir
- Changed primary jar to name-version.jar, & linked.
- Added clean tarball generator 

* Wed Dec 03 2008 <mycae(a!t)yahoo.com> 6.7-5
- Added LICENSE_nanoxml
- Updated licence spec line to include ASL 1.1 & zlib
- removed Clock.java due to incompatible license

* Sat Nov 29 2008 <mycae(a!t)yahoo.com> 6.7-4
- Updated BuildRequires to inlcude laf-plugin
- Silence several rpmlint errors
	- ASL 2.0 vs Apache Source Licence 2.0
	- Fix arch
	- Fix EOL on docs.

* Sun Nov 23 2008 <mycae(a!t)yahoo.com> 6.7-3
- Modify description field

* Sun Nov 16 2008 <mycae(a!t)yahoo.com> 6.7-2
- Fix version numbering
- Fix top level dir when building jar 

* Sat Nov 01 2008 <mycae(a!t)yahoo.com> 6.7-1
- Create spec file

