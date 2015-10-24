Summary:	GNOME Getting Started guide
Summary(pl.UTF-8):	Podręcznik wprowadzający do środowiska GNOME
Name:		gnome-getting-started-docs
Version:	3.18.1
Release:	1
License:	CC-BY-SA-3.0
Group:		Documentation
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-getting-started-docs/3.18/%{name}-%{version}.tar.xz
# Source0-md5:	0bbf2f41275b25d27da6ea4736b25e3d
URL:		http://live.gnome.org/DocumentationProject
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.11
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.198
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	yelp-tools
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains the Getting Started guide.

%description -l pl.UTF-8
Ten pakiet zawiera podręcznik "Getting Started", wprowadzający do
środowiska GNOME.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang gnome-help --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f gnome-help.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING NEWS README
