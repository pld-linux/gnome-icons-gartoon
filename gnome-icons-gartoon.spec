#
%define 	realname gartoon
#
Summary:	Gartoon GNOME Icons
Summary(pl.UTF-8):	Zestaw ikonek Gartoon dla GNOME
Name:		gnome-icons-gartoon
Version:	0.5
Release:	2
License:	GPL v2
Group:		X11/Amusements
Source0:	http://zeus.qballcow.nl/icon/paket/%{realname}-%{version}.tar.gz
# Source0-md5:	19fd88682ad2f88ca85f7e0a904610fd
URL:		http://zeus.qballcow.nl/
BuildRequires:	gtk-update-icon-cache
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gartoon is a fun looking icon pack for GNOME desktop environment.

%description -l pl.UTF-8
Gartoon jest zestawem śmiesznie wyglądających ikonek dla GNOME.

%prep
%setup -q -n %{realname}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_iconsdir}/%{realname}

cp -af . $RPM_BUILD_ROOT%{_iconsdir}/%{realname}

gtk-update-icon-cache -ft $RPM_BUILD_ROOT%{_iconsdir}/%{realname}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README gartoon-pallete.svg
%dir %{_iconsdir}/%{realname}
%dir %{_iconsdir}/%{realname}/scalable
%dir %{_iconsdir}/%{realname}/scalable/apps
%dir %{_iconsdir}/%{realname}/scalable/devices
%dir %{_iconsdir}/%{realname}/scalable/emblems
%dir %{_iconsdir}/%{realname}/scalable/filesystems
%dir %{_iconsdir}/%{realname}/scalable/mimetypes
%dir %{_iconsdir}/%{realname}/scalable/stock
%dir %{_iconsdir}/%{realname}/scalable/stock/Xtra
%{_iconsdir}/%{realname}/index.theme
%{_iconsdir}/%{realname}/scalable/apps/*.svg
%{_iconsdir}/%{realname}/scalable/devices/*.svg
%{_iconsdir}/%{realname}/scalable/emblems/*.svg
%{_iconsdir}/%{realname}/scalable/emblems/*.icon
%{_iconsdir}/%{realname}/scalable/filesystems/*.svg
%{_iconsdir}/%{realname}/scalable/filesystems/*.icon
%{_iconsdir}/%{realname}/scalable/mimetypes/*.svg
%{_iconsdir}/%{realname}/scalable/stock/*.svg
%{_iconsdir}/%{realname}/scalable/stock/Xtra/*.svg
%{_iconsdir}/%{realname}/scalable/stock/iconrc
%{_iconsdir}/%{realname}/icon-theme.cache
